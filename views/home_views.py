import flask
import sys
import os
from badgettingbetter.infrastructure.view_modifiers import response
from badgettingbetter.viewmodels.home.index_viewmodel import IndexViewModel

blueprint = flask.Blueprint('home', __name__, template_folder='templates')

@blueprint.route('/')
@response(template_file="home/index.html")
def home():
    vm = IndexViewModel()
    return vm.to_dict()

@blueprint.route('/index')
@response(template_file="home/index.html")
def index():
    vm = IndexViewModel()
    return vm.to_dict()

@blueprint.route('/about')
@response(template_file="home/about.html")
def about():
    vm = IndexViewModel()
    return vm.to_dict()

@blueprint.route('/todo')
@response(template_file="home/todo.html")
def todo():
    vm = IndexViewModel()
    return vm.to_dict()