from flask import Flask, render_template, request, redirect, url_for, make_response
import json
from datetime import datetime, timedelta
from database import *

app = Flask(__name__)

@app.route('/')
def index():
    comments = db.get_comments()
    expiration_date = datetime.now() + timedelta(days=36500)
    response = make_response(render_template('index.html',comments=comments))
    if 'session' not in request.cookies:
        response.set_cookie('session',db.get_new_session(),expires=expiration_date)
    return response

@app.route('/submit', methods=['POST'])
def submit():
    user_agent = request.headers.get('User-Agent')
    if 'session' in request.cookies and 'name' in request.form and 'comment' in request.form:
        data = request.form
        if len(data["comment"]) > 8192 or len(data["name"]) > 32:
            return "Comment Size or name exceeds maximum length. Please be concise"
        try:
            db.add_comment(data["name"],data["comment"],request.cookies['session'],user_agent)
        except:
            pass
    return redirect(url_for('index'))

try:
    db.init_db()
except:
    print('database already init')

if __name__ == '__main__':
    app.run(debug=True,port=5001)