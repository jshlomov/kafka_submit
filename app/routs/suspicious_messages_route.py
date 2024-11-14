from flask import Blueprint, request, jsonify

from app.repository.postgres_repository.person_repository import get_person_by_email
from app.services.producers.message_producer import produce_message

messages_blueprint = Blueprint('/messages', __name__)


@messages_blueprint.route('/messages/<string:email>', methods=['GET'])
def new_member(email):
    get_person_by_email(email)
    return jsonify(), 200