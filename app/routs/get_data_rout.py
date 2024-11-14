from flask import Blueprint, request, jsonify

from app.repository.mongo_repository import insert_message

data_blueprint = Blueprint('data', __name__)


@data_blueprint.route('/email', methods=['POST'])
def new_member():
    message = request.json
    print(message)
    insert_message(message)
    return jsonify("info for new member recived"), 200