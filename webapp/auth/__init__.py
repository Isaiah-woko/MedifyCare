from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_login import AnonymousUserMixin, login_user
from flask_dance.contrib.facebook import make_facebook_blueprint, facebook
from flask_dance.consumer import oauth_authorized
from flask import flash, redirect, url_for, session, abort
from flask_dance.contrib.google import make_google_blueprint, google

"""patch google login problem"""

# Patch for Flask-Dance compatibility with Flask >= 2.3
from flask import current_app

def _lookup_app_object(name):
    return getattr(current_app, name, None)

from flask.globals import LocalProxy

""""""
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.session_protection ="strong"
login_manager.login_message = "Please login to access this page"
login_manager.login_message_category = "info"

class BlogAnonymous(AnonymousUserMixin):
    def __init__(self):
        self.username = 'Guest'

@login_manager.user_loader
def load_user(userid):
    from .models import User
    return User.query.get(userid)


# create the auth
def auth_create_module(app,**kwargs):
    bcrypt.init_app(app)
    login_manager.init_app(app)
    from .view import auth_blueprint
    app.register_blueprint(auth_blueprint)
    facebook_blueprint = make_facebook_blueprint(
    client_id=app.config.get("FACEBOOK_CLIENT_ID"),
    client_secret=app.config.get("FACEBOOK_CLIENT_SECRET"),
    )
    app.register_blueprint(facebook_blueprint, url_prefix="/auth/login")

@oauth_authorized.connect
def logged_in(blueprint, token):
    ## info it just login without password just by adding the username
    from .models import db, User
    if blueprint.name == 'facebook':
        resp = facebook.get("/me")
        username = resp.json()['name']
    user = User.query.filter_by(username=username).first()
    if not user:
        user = User()
        user.username = username
        db.session.add(user)
        db.session.commit()
    login_user(user)
    flash("You have been logged in.", category="success")
