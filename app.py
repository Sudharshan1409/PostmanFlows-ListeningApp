from flask import Response, jsonify, request, render_template, redirect
from db import app, db, RedirectUrls, Blog
import markdown
from urllib.parse import urljoin


@app.route('/', methods=['GET', 'POST'])
def home_page():
    if request.method == 'POST':
        dropbox_url = request.form.get('dropboxRedirectUrl')
        print('URL', dropbox_url)
        redirect_url = RedirectUrls(dropboxUrl=dropbox_url)
        urls = RedirectUrls.query.all()
        if urls:
            url = urls[0]
            # update the url
            url.dropboxUrl = dropbox_url
            db.session.commit()
        else:
            db.session.add(redirect_url)
            db.session.commit()
        return redirect('/')
    else:
        base_url = request.base_url
        dropbox_webhook_handle_url = base_url + 'dropbox/webhookhandler'
        urls = RedirectUrls.query.all()
        if urls:
            url = urls[0].dropboxUrl
        else:
            url = ''
        return render_template('index.html', dropbox_url=url, dropbox_webhook_url=dropbox_webhook_handle_url)


@app.route('/blog', methods=['POST', 'GET'], defaults={'blog_id': None})
@app.route('/blog/<int:blog_id>', methods=['GET'])
def blogPage(blog_id=None):
    if request.method == 'POST':
        base_url = request.base_url
        title = request.json.get('title')
        content = request.json.get('content')
        blog = Blog(title=title, content=content)
        db.session.add(blog)
        db.session.commit()
        blog_url = urljoin(base_url, f"blog/{blog.id}")
        return jsonify({'status': 'success', 'message': 'Blog added successfully', 'url': f"{blog_url}"}), 201
    else:
        if blog_id:
            blog = Blog.query.get(blog_id)
            if blog:
                blog_content = markdown.markdown(blog.content)
                return render_template('blog.html', blog_text=blog_content, blog_title=blog.title)
            else:
                return Response('Blog not found', status=404)
        else:
            # blogs = Blog.query.all()
            # html_data = ''
            # for blog in blogs:
            #     html_data += f'<h2>{blog.title}</h2>'
            #     html_data += markdown.markdown(blog.content)
            return Response('Not yet implemented', status=501)


@app.route('/dropbox/webhookhandler', methods=['GET', 'POST'])
def dropbox_webhook_handler():
    # if get request
    if request.method == 'GET':
        if 'challenge' not in request.args:
            return Response('Invalid request, no challenge present in the request', status=400)
        resp = Response(request.args.get('challenge'))
        resp.headers['Content-Type'] = 'text/plain'
        resp.headers['X-Content-Type-Options'] = 'nosniff'
        return resp
    else:
        print("Request in dropbox handler", request.json)
        urls = RedirectUrls.query.all()
        if urls:
            url = urls[0].dropboxUrl
            return redirect(url)
        else:
            resp = Response('No URL found', status=400)
            return resp


@app.route('/facebook/webhookhandler', methods=['GET', 'POST'])
def facebook_webhook_handler():
    # if get request
    if request.method == 'GET':
        print("Request in facebook handler", request.args)
        return Response(request.args.get('hub.challenge'))
    else:
        print("Request in facebook handler", request.json)
        return Response('Success')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
