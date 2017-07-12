"""Properties view functions."""
from flask import Blueprint, current_app, jsonify, request

from .db import create_filter


bp = Blueprint('properties', __name__)


@bp.route('/properties', methods=['GET'])
def list_properties():
    """Properties resource.

    If the GET request is called with no parameters then all the properties
    are returned. Otherwise returns the properties matched by the query
    parameters of the GET request.

    Returns:
        An http response with the results serialized in json.

    """
    kwargs = {
        'filter': create_filter(request.args) or None,
        'projection': {
            '_id': False,
        }
    }
    properties = current_app.db.properties.find(**kwargs)
    return jsonify(list(properties))
