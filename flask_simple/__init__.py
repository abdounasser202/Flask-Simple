from flask import Blueprint

class Simple(object):
    def __init__(self, app):
        self.app = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        simple = self.register('simple')
        app.register_blueprint(simple)

    def register(self, name):
        feature = Blueprint(name,
                        __name__,
                        template_folder='templates',
                        static_folder='static',
                        url_prefix='/simple')
        feature.add_url_rule('/hello/<name>', view_func=self.hello)
        return feature

    def hello(self, name):
        return 'hello ' + ' ' + name
