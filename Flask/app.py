from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('hello_world.html')

@app.route('/', methods=['Get, Post'])
def index():
    pass

if __name__ == '__main__':
    app.run(debug=True)