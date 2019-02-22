""" Auth views. """

from flask import Blueprint, render_template

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register')
def register():
    # Register a new user
    title = 'Register'
    return render_template('auth/register.html', title=title)
