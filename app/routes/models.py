from flask import Blueprint, jsonify
from app.config.config import OPENROUTER_MODEL

models_bp = Blueprint("models", __name__)

@models_bp.route("/models", methods=["GET"])
def get_models():
    """
    Get available models
    ---
    tags:
      - Models
      
    responses:
      200:
        description: Successfully retrieved available models

      400:
        description: Invalid request

    500:
        description: Internal server error
    """
    return jsonify({
        "success": True,
        "current_model": OPENROUTER_MODEL
    }), 200