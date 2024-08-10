from flask import (Blueprint, request, session, flash, redirect, url_for, render_template)

from db.db import db
from models.model import *

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            pass

    return render_template('login.html')
