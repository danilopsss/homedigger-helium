from flask import request, jsonify, Blueprint
from helium.services.utils.api_types import ApiResponse
from helium.services.authservice.schemas import UserSchema
from helium.services.authservice.utils import create_db_event


auth_bp = Blueprint("authservice", __name__, url_prefix="/auth")


@auth_bp.route("/register", methods=["POST"])
def register_user():
    try:
        event = create_db_event(request, "USER_CREATED")
        user_data = {**request.json, **event}
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
