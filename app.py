from flask import Flask, render_template, request, redirect, url_for
import json
from database import *

app = Flask(__name__)

@app.route('/')
def index():
    global db
    comments = db.get_comments()
    return render_template('index.html',comments=comments)

@app.route('/submit', methods=['POST'])
def submit():
    global db
    data = request.form
    db.add_comment(data["name"],data["comment"])
    return redirect(url_for('index'))

if __name__ == '__main__':
    global db
    db = database("database.config")
    try:
        db.init_db()
    except:
        print('database already init')
    app.run(debug=True,port=5001)