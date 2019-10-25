import json
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client['NHL']
collection_currency = db['NHLdata']

with open('nhl.json') as f:
    file_data = json.load(f)

# use collection_currency.insert(file_data) if pymongo version < 3.0
collection_currency.insert_many(file_data)  
client.close()