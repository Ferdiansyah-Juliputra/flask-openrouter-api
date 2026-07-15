from flask import Flask, render_template
from app.routes.chat import chat_bp
from app.routes.health import health_bp
from app.routes.models import models_bp
from app.error_handler import register_error_handlers

def create_app():
    app = Flask(__name__)
    app.register_blueprint(chat_bp)
    app.register_blueprint(health_bp)
    app.register_blueprint(models_bp)
    register_error_handlers(app)

    @app.route('/')
    def index():
        return render_template('index.html')
    
    return app