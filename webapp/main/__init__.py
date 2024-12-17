def main_create_module(app,**kwargs):
    from .view import main_blueprint
    app.register_blueprint(main_blueprint)

