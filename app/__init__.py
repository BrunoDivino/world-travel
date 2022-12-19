from flask import Flask
from dynaconf import FlaskDynaconf

# application factory:

def create_app():
    app = Flask(__name__)
    FlaskDynaconf(app, extensions_list=True)

    return app