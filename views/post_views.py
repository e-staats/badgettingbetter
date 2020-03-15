import flask
from flask import jsonify
from badgettingbetter.infrastructure.view_modifiers import response
import badgettingbetter.infrastructure.request_dict as request_dict
# pylint: disable=no-member

blueprint = flask.Blueprint('post', __name__, template_folder='templates')


# ################### POST PAGES #################################

@blueprint.route('/posts')
@response(template_file='posts/index.html')
def post_home():

    return {}

# ################### POST PAGES #################################

@blueprint.route('/posts/struggles-with-python-path')
@response(template_file='posts/struggles-with-python-path.html')
def post_page():
    return {}