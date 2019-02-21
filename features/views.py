""" Views for features app. """

from flask import Blueprint, render_template

bp = Blueprint('features', __name__)


@bp.route('/')
def index():
    # Render home page
    return render_template('features/index.html')
