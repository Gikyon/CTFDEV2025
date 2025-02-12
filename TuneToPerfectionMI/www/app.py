from flask import Flask, render_template, request, make_response
import os

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def login():
    message = ''
    if request.method == 'POST':
        message = 'no account is registered'
        cookie = request.cookies.get('secret')
        if cookie == 'cGV0ZXI6cm9zZWFubmU=':
            message = 'bhbureau{dontyouwantmelikeiwantyoubaby\}'
        return render_template('login.html', message=message)
            
    else:
        res = make_response(render_template('login.html', message=message))
        res.set_cookie("secret", value="bWFsZTpmZW1hbGU")
        return res


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 80))  # Default to 8000 if PORT is not set
    app.run(debug=False, host='0.0.0.0', port=port)
