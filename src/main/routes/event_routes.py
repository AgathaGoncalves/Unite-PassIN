# pylint: disable-all
from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest

event_route_bp = Blueprint('event_route', __name__)

@event_route_bp.route('/events', methods=['POST'])
def get_events():
    http_request = HttpRequest(body=request.json)
    return  jsonify({"helooooo": "woooord"}),200