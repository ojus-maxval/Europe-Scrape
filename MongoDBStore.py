from pymongo import MongoClient, collection
from pymongo.message import insert

class Mongo:

    #to setup connection with MongoDB
    def __init__(self, str):
        self.client=MongoClient(str)

    #to get column of MongoDB database where we want to perform database operations
    def getCol(self, dbs, clientDbs):
        db=self.client[dbs]
        col=db[clientDbs]
        return col

    #to insert one document in MongoDB 
    def insertOne(self,str,col):
        return col.insert_one(str)

    #to insert many documents in MongoDB
    def insertMany(self,strs,col):
        return col.insert_many(strs)

    #to read documents in MongoDB
    def read(self,conditions,col):
        return col.find_one(conditions)