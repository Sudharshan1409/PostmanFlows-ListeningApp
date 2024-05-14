import requests
from flask import Response, request, render_template, redirect
from db import app, db, RedirectUrls


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


@app.route('/dropbox/webhookhandler', methods=['GET', 'POST'])
def dropbox_webhook_handler():
    # if get request
    if request.method == 'GET':
        if 'challenge' not in request.args:
            return Response('Invalid request', status=400)
        resp = Response(request.args.get('challenge'))
        resp.headers['Content-Type'] = 'text/plain'
        resp.headers['X-Content-Type-Options'] = 'nosniff'
        return resp
    else:
        print("Request", request.json)
        urls = RedirectUrls.query.all()
        if urls:
            url = urls[0].dropboxUrl
            return redirect(url)
        else:
            resp = Response('No URL found', status=400)
            return resp


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
