import flask
import os
import sys
folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)

app = flask.Flask(__name__)

def main():
    register_blueprints()
    print(os.getcwd())
    app.run(debug=True)
    

# def register_blueprints():
#     from views import home_views
#     app.register_blueprint(home_views.blueprint)

def register_blueprints():
    from badgettingbetter.views import post_views
    from badgettingbetter.views import home_views

    app.register_blueprint(home_views.blueprint)
    app.register_blueprint(post_views.blueprint)


if __name__=="__main__":
    main()