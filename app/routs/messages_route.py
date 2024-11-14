from flask import Blueprint, jsonify

from app.services.person_message_service import get_person_messages_by_email

messages_blueprint = Blueprint('messages', __name__)


@messages_blueprint.route('/messages/<string:email>', methods=['GET'])
def new_member(email):
    person = get_person_messages_by_email(email)
    return person, 200