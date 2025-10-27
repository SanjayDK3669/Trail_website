from marshmallow import Schema, fields, validate, ValidationError

def validate_phone(n):
    if n is None or n == "":
        return True
    cleaned = "".join(ch for ch in n if ch.isdigit())
    if len(cleaned) < 7 or len(cleaned) > 15:
        raise ValidationError("Phone must contain 7-15 digits.")
    return True

class ContactSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=2, max=255))
    email = fields.Email(required=True, validate=validate.Length(max=255))
    phone = fields.Str(required=False, allow_none=True, validate=validate_phone)
    message = fields.Str(required=False, allow_none=True, validate=validate.Length(max=2000))
