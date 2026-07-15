from flask import Blueprint, jsonify
from config.config import OPENROUTER_MODEL

health_bp = Blueprint("health", __name__)

@health_bp.route("/health", methods=["GET"])
def health():
    return jsonify({
        "success": True,
        "data": {
            "status": "healthy"
        },
        "service": "OpenRouter Flask API",
        "model": OPENROUTER_MODEL
    }), 200