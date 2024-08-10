from flask import (Flask, render_template, request)

from db.db import db
from models import *
from controllers import auth

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secert!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

    return render_template("login.html")


app.register_blueprint(auth.bp)

if __name__ == '__main__':
    app.run()
