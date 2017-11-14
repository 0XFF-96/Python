""" rmon.views.urls

"""

from flask import Blueprint
from rmon.views.index import IndexView

api = Blueprint('api', __name__)

api.add_url_rule('/',view_func = IndexView.as_view('index'))


