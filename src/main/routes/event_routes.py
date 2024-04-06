# pylint: disable-all
from flask import Blueprint, jsonify

event_route_bp = Blueprint('event_route', __name__)

@event_route_bp.route('/events', methods=['POST'])
def get_events():
    return  jsonify({"helooooo": "woooord"}),200