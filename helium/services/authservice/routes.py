from flask import request, jsonify, Blueprint
from helium.core.utils.secrets import Secrets
from helium.services.utils.api_types import ApiResponse
from helium.services.authservice.schemas import UserSchema
from helium.services.authservice.utils import create_db_event
from helium.services.authservice.models.user_access_history import Events


auth_bp = Blueprint("authservice", __name__, url_prefix="/auth")


@auth_bp.route("/register", methods=["POST"])
def register_user():
    try:
        event = create_db_event(request, Events.USER_CREATED.value)
        parsed_secret = Secrets(request.json.pop("secrets")).process_secret()
        user_data = {**request.json, **event, **parsed_secret}
        new_user = UserSchema(**user_data).save()
        return (
            jsonify(
                {
                    "user": new_user.username,
                    "status": ApiResponse.CREATED.message,
                }
            ),
            ApiResponse.CREATED.code,
        )
    except Exception as e:
        # TODO: track the errors in order to provide adequate
        # exception handling with appropriate error codes.
        return {"error": str(e)}, 500


@auth_bp.route("/authenticate", methods=["POST"])
def generate_token():
    return {}, 200
