from flask import (Flask, render_template, request)

from db.db import db
from models import *
from controllers import auth

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")


@app.route('/about', methods=['GET', 'POST'])
def about(): return render_template("about.html")


app.register_blueprint(auth.bp)

if __name__ == '__main__':
    app.run()
