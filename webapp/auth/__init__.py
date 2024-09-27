from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_login import AnonymousUserMixin
from flask_dance.contrib.facebook import make_facebook_blueprint, facebook



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
    facebook_blueprint = make_facebook_blueprint(
    client_id=app.config.get("FACEBOOK_CLIENT_ID"),
    client_secret=app.config.get("FACEBOOK_CLIENT_SECRET"),
    )
    from .view import auth_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(facebook_blueprint, url_prefix="/auth/login")
