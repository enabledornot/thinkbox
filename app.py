from flask import Flask, render_template
import json


app = Flask(__name__)


@app.route('/')
def hello():
    with open("default.json","r") as f:
        comments = json.load(f)
    return render_template('index.html',comments=comments)

if __name__ == '__main__':
    app.run(debug=True,port=5001)