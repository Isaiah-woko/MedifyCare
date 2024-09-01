from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_socketio import SocketIO
db = SQLAlchemy()
migrate = Migrate()
socketio = SocketIO()

def create_app(object_name):
 
    app = Flask(__name__)
    app.config.from_object(object_name)
    db.init_app(app)
    migrate.init_app(app, db)
    socketio.init_app(app)
    from .main import main_create_module
    from .auth import auth_create_module
    from .chat import chat_create_module
    from .payment import payment_create_module
    main_create_module(app)
    auth_create_module(app)
    chat_create_module(app)
    payment_create_module(app)
    return app
