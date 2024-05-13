import requests
from flask import Response, request, render_template
from db import app, db, RedirectUrls


@app.route('/', methods=['GET', 'POST'])
def home_page():
    if request.method == 'POST':
        dropbox_url = request.form.get('dropboxRedirectUrl')
        print('URL', dropbox_url)
        redirect_url = RedirectUrls(dropboxUrl=dropbox_url)
        urls = RedirectUrls.query.all()
        if urls:
            for url in urls:
                db.session.delete(url)
        db.session.add(redirect_url)
        db.session.commit()
        return render_template('index.html', dropbox_url=dropbox_url)
    else:
        urls = RedirectUrls.query.all()
        if urls:
            url = urls[0].dropboxUrl
        else:
            url = ''
        return render_template('index.html', dropbox_url=url)


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
        requests.post('https://5425a7ac396349f0b45fdf58e85816f0.flow.pstmn.io/')
        resp = Response('OK')

    return resp


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
