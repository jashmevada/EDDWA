from flask import (Blueprint, request, session, flash, redirect, url_for, render_template)

from db.db import db
from models.model import *

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['psw']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            pass

    return render_template('login_page.html')


@bp.route('/logout', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['psw']
        email = request.form['email']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            pass
    return render_template("sign_up.html")