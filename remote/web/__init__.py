import os
from flask import Flask
from . import index

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.environ['SECRET_KEY'],
    )

    app.register_blueprint(index.bp)
    return app
