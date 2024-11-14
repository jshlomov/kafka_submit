import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv(verbose=True)

client = MongoClient(os.environ['MONGO_DB_URL'])

db = client['messages']
all_messages_coll = db['all_messages']
