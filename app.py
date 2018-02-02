from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/feed')
def feed():
    return render_template("feed.html")

@app.route('/post')
def post():
    return render_template("post.html")

@app.route('/signin')
def signin():
    return render_template("signin.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)


