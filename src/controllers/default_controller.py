from flask import Blueprint

default = Blueprint('default', __name__)


@default.route('/')
def health():
    return {'status': 'Alive'}

