from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_socketio import SocketIO
from flask_mailman import Mail
db = SQLAlchemy()
migrate = Migrate()
socketio = SocketIO()
mail = Mail()

def create_app(object_name):

    app = Flask(__name__)
    app.config.from_object(object_name)
    app.config['SECRET_KEY'] = 'thisismysecretkey'
    app.config['RSET_PASS_TOKEN_MAX_AGE'] = 3600
    app.config['UPLOAD_FOLDER'] = 'webapp/static/images/'
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'medifycare24@gmail.com'
    app.config['MAIL_DEFAULT_SENDER'] = 'medifycare24@gmail.com'
    app.config['MAIL_PASSWORD'] = 'mlxcmevqstukhfoa'

    db.init_app(app)
    migrate.init_app(app, db)
    socketio.init_app(app)
    mail.init_app(app)
    from .main import main_create_module
    from .auth import auth_create_module
    from .chat import chat_create_module
    # from .payment import payment_create_module
    main_create_module(app)
    auth_create_module(app)
    chat_create_module(app)
    # payment_create_module(app)
    with app.app_context():
        db.create_all()
    return app
