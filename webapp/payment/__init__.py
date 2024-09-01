def payment_create_module(app,**kwargs):
    from .view import payment_blueprint
    app.register_blueprint(payment_blueprint)

