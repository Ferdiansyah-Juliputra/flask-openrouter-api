from flask import Flask, render_template
from flasgger import Swagger

from app.error_handler import register_error_handlers

from app.routes.health import health_bp
from app.routes.resume import resume_bp
from app.routes.review import review_bp


def create_app():
    app = Flask(__name__)

    swagger_template = {
        "swagger": "2.0",
        "info": {
            "title": "AI Resume Reviewer API",
            "description": "REST API for AI-powered resume analysis, ATS scoring, and recommendations.",
            "version": "1.0.0"
        }
    }

    Swagger(app, template=swagger_template)

    # Register Blueprints
    app.register_blueprint(health_bp)
    app.register_blueprint(resume_bp)
    app.register_blueprint(review_bp)

    register_error_handlers(app)

    @app.route("/")
    def index():
        return render_template("index.html")

    return app