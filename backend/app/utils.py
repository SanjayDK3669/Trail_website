from flask import jsonify
from marshmallow import ValidationError

def handle_validation_error(e: ValidationError):
    return jsonify({"error": "validation_error", "messages": e.messages}), 400
