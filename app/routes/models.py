from flask import Blueprint, jsonify
from config.config import OPENROUTER_MODEL

models_bp = Blueprint("models", __name__)

@models_bp.route("/models", methods=["GET"])
def get_models():
    return jsonify({
        "success": True,
        "current_model": OPENROUTER_MODEL
    }), 200