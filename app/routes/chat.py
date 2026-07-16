from flask import Blueprint, jsonify, request
from app.services.openrouter_services import generate_response
from app.logger.logger import logger

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/chat", methods=["POST"])
def chat():
    """
    Generate AI response
    ---
    tags:
      - Chat

    consumes:
      - application/json

    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            message:
              type: string
              example: Hello!

    responses:
      200:
        description: Response generated successfully

      400:
        description: Invalid request

      500:
        description: Internal server error
    """

    logger.info(f"Received request: {request.method} {request.path}")

    # if request.method == "GET":
    #     return jsonify({
    #         "reply": "temporary response"
    #     })

    body = request.get_json(silent=True)

    if body is None or "message" not in body:
        logger.warning("Invalid request: Missing 'message' in request body")

        return jsonify({
            "success": False,
            "message": "Invalid request. Please provide a 'message' in the request body."
        }), 400
    
    prompt = body.get("message", "")

    if not prompt.strip():
        logger.warning("Invalid request: Prompt is required")

        return jsonify({
            "success": False,
            "message": "Prompt is required."
        }), 400

    logger.info("Sending prompt to OpenRouter API for response generation")

    reply = generate_response(prompt)
    
    logger.info(f"Successfully generated reply ({len(reply)} characters)")

    return jsonify({
        "success": True,
        "data": {
            "reply": reply      
        }
    }), 200



