import os
from flask import Flask
from . import index, backend

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.environ['SECRET_KEY'],
    )

    app.register_blueprint(index.bp)
    app.register_blueprint(backend.bp)
    return app
