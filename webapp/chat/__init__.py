def chat_create_module(app, **kwargs):
    from .view import chat_blueprint
    app.register_blueprint(chat_blueprint)
