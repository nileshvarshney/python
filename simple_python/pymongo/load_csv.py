from pymongo import MongoClient
from Connection import Connect
import pandas as pd
import json


# Read the csv file in pandas dataframe
data = pd.read_csv("./sample_201501.csv")

# convert data in json format before loading to mongodb
data_json = json.loads(data.to_json(orient='records'))

conn = Connect.get_connection()
db=conn['foobar']
coll = db['flights']
coll.remove()
coll.insert_many(data_json)

print(coll.find_one())
