from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ssdasdadsdasd'
    from .controllers.default_controller import default
    from .controllers.jobs_controller import jobs
    app.register_blueprint(default, url_prefix='/')
    app.register_blueprint(jobs, url_prefix='/')

    return app

