from flask import Flask
from app.api import display


def create_app():
    app = Flask(__name__)

    return app
