from flask import Flask, render_template, request, redirect, url_for
import json
from database import *

app = Flask(__name__)

@app.route('/')
def index():
    comments = db.get_comments()
    return render_template('index.html',comments=comments)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form
    db.add_comment(data["name"],data["comment"])
    return redirect(url_for('index'))

try:
    db.init_db()
except:
    print('database already init')

if __name__ == '__main__':
    app.run(debug=True,port=5001)