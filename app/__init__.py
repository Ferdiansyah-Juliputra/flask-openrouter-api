from flask import Flask, render_template
from flasgger import Swagger
from app.routes.chat import chat_bp
from app.routes.health import health_bp
from app.routes.models import models_bp
from app.error_handler import register_error_handlers

def create_app():
    app = Flask(__name__)

    swagger_template = {
        "swagger": "2.0",
        "info": {
            "title": "OpenRouter Flask API",
            "description": "API for interacting with OpenRouter",
            "version": "1.0.0"
        }
    }

    Swagger(app, template=swagger_template)

    app.register_blueprint(chat_bp)
    app.register_blueprint(health_bp)
    app.register_blueprint(models_bp)
    register_error_handlers(app)

    @app.route('/')
    def index():
        return render_template('index.html')
    
    return app