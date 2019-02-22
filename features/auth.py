""" Auth views. """

from flask import Blueprint, render_template

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register')
def register():
    # Register a new user
    title = 'Register'
    return render_template('auth/register.html', title=title)


@bp.route('/login')
def login():
    # Log in a registered user
    title = 'Login'
    return render_template('auth/login.html', title=title)
