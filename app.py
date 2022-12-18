from flask import Flask

# application factory:

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Hello Flask'

    return app