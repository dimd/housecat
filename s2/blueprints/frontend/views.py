"""Frontend view functions."""
from flask import Blueprint, current_app

bp = Blueprint('frontend',
               __name__,
               static_folder='static',
               static_url_path='')


@bp.route('/', methods=['GET'])
def index():
    return current_app.send_static_file('index.html')
