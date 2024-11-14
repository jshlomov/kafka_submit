from flask import Blueprint, request, jsonify


data_blueprint = Blueprint('data', __name__)


@data_blueprint.route('/email', methods=['POST'])
def new_member():
    mem = request.json
    return jsonify("info for new member recived"), 200