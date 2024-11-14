from flask import Blueprint, request, jsonify

from app.services.producers.message_producer import produce_message

data_blueprint = Blueprint('data', __name__)


@data_blueprint.route('/email', methods=['POST'])
def new_member():
    message = request.json
    produce_message(message)
    return jsonify("info for new member recived"), 200