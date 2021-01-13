from pymongo import MongoClient

class Connect(object):
    @staticmethod
    def get_connection():
        return MongoClient(port=27017)

connection = Connect.get_connection()
db = connection.foobar
print(db.foo.find().count())

