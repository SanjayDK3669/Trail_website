from flask import Blueprint, request, jsonify, current_app
from .models import db, Contact
from .schemas import ContactSchema
from .utils import handle_validation_error
from marshmallow import ValidationError
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

api_blueprint = Blueprint("api", __name__)
contact_schema = ContactSchema()

@api_blueprint.route("/submit", methods=["POST"])
def submit_contact():
    """
    Accepts JSON: { name, email, phone?, message? }
    """
    try:
        payload = request.get_json(force=True)
    except Exception:
        return jsonify({"error": "invalid_json"}), 400

    try:
        data = contact_schema.load(payload)
    except ValidationError as e:
        return handle_validation_error(e)

    # Create and persist
    contact = Contact(
        name=data["name"].strip(),
        email=data["email"].strip().lower(),
        phone=(data.get("phone") or "").strip(),
        message=(data.get("message") or "").strip()
    )

    try:
        db.session.add(contact)
        db.session.commit()
    except Exception as e:
        current_app.logger.exception("DB error when inserting contact")
        db.session.rollback()
        return jsonify({"error": "db_error", "detail": str(e)}), 500

    # Respond with minimal data
    return jsonify({"status": "success", "id": contact.id}), 201
