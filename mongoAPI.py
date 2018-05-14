import pymongo
import base64
from bson.objectid import ObjectId
class mongoAPI:
    def __init__(self,collection):
        db_host = "10.3.242.91"
        db_port = 27017
        client = pymongo.MongoClient(db_host,db_port)
        db_auth = client.tcExp
        db_auth.authenticate("tcExp", "root")
        db = client.tcExp
        self.collection = db.get_collection(collection)

    def collectionInsert(self,content,label,labelname,source,url):
        dict1 = {"content": content,"label":label,"labelname":labelname,"source":source,"url":url}
        #print(dict1)
        self.collection.insert_one(dict1)

    def collectionFind(self,query):
        result = self.collection.find(query)
        return result

    def collectionUpdate(self,id,fenci):
        self.collection.update_one({"_id": ObjectId(id)},{"$set":{"fenci":fenci}})
    
    def collectionUpdateContent(self,id,content):
        self.collection.update_one({"_id": ObjectId(id)},{"$set":{"content":content}})

if __name__ == '__main__':
    mongo = mongoAPI('news')
    print(mongo.collectionFind({'fenci':{'$exists':False}}).count())
