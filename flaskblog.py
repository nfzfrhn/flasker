from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/about')
def about():
    return '<h1>About Page</h1>'


@app.route('/about/<username>')
def about_user(username):
    return f'<h1>About {username}</h1>'