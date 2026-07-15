from flask import jsonify
def register_error_handlers(app):

    @app.errorhandler(Exception)
    def handle_exception(error):
        return jsonify({
            "success": False,
            "message": str(error)
        }), 500
    