import json
from flask import jsonify, request, Blueprint
from gatekeeper.core.utils.decorators import resolve_proxy_path
from gatekeeper.services.proxy.authservice.schemas import ProxyAuthSchema


proxy_bp = Blueprint('proxy', __name__, url_prefix='/gk')


@proxy_bp.route('/authenticate', methods=["POST"])
@resolve_proxy_path
def check_compass():
    request_received = request.data.decode('utf-8')
    data = json.loads(request_received)
    return ProxyAuthSchema(**data)
