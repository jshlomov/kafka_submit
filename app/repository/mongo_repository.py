from app.db.mongo_db import all_messages_coll


def insert_message(message):
    all_messages_coll.insert_one(message)