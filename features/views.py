""" Views for features app. """

from flask import Blueprint, render_template

bp = Blueprint('features', __name__)


@bp.route('/')
def index():
    # Render home page
    title = 'Home'
    return render_template('features/index.html', title=title)
