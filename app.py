from flask import Flask, Blueprint

# application factory:

def create_app():
    app = Flask(__name__)

    home = Blueprint('home', __name__)

    @home.route('/')
    def index():
        return 'Hello Flask'

    app.register_blueprint(home)

    return app