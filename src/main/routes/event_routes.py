# pylint: disable-all
from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.data.event_handler import EventHandler

event_route_bp = Blueprint('event_route', __name__)

@event_route_bp.route('/events', methods=['POST'])
def crate_event():
    http_request = HttpRequest(body=request.json)
    event_handler = EventHandler()

    http_response = event_handler.register(http_request)
    return jsonify(http_response.body),http_response.status_code

@event_route_bp.route('/events/<event_id>', methods=['GET'])
def get_events(event_id):
    event_handler = EventHandler()
    http_request = HttpRequest(param={"event_id": event_id})

    http_response = event_handler.find_by_id(http_request)
    return jsonify(http_response.body),http_response.status_code
