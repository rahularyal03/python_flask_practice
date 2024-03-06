from dbconnect import db 
from datetime import datetime
from bson import ObjectId 

class User(object):
    def __init__(self, data):
        self.name = data.get("name")
        self.password = data.get("password")
        self.phone = data.get("phone", [])
        self.created_at = str(datetime.utcnow())
    
    
    def save_to_db(self):
       data = db.users.insert_one({
            "name": self.name,
            "password": self.password,
            "phone": self.phone,
            "created_at": self.created_at
        })
       
       return data
        
     
    @staticmethod
    def get_all_users():
        
        data = db.users.find({})
        return data
    
    @staticmethod
    def find_user(id):
        object_id = ObjectId(id)
        data = db.users.find_one({"_id": object_id})
       
        return data
    
    
    def update_user_info(self, id):
        object_id = ObjectId(id)
        data = db.users.update_one({"_id": object_id}, {"$set":{
            "name": self.name,
            "password": self.password,
            
        }, "$push":{"phone": self.phone}})
        return data
    
    def delete_user_by_id(id):
        data = db.users.delete_one({"_id": ObjectId(id)})
        return data
    
     
    @staticmethod
    def get_data(name):
        user_name = name.split("+")
        user = " ".join(user_name)
        print(user)
        
        # It will display all the users.
        # data = db.users.find({"name": user})
        
        # It will display all the user with that query name and only display the phone number and the userId
        # data = db.users.find({"name": user}, {"phone": 1})
        
        
        # Here 0 is for exclude and 1 is to include
        data = db.users.find({"name": user}, {"password": 0}).limit(2)
        
        
        # limiting the query without sorting
        # data = db.users.find({"name": user}, {"phone": 1}).limit(2)
        
        # limiting the query with sorting
        # data = db.users.find({"name": user}, {"phone": 1}).sort({"phone": 1}).limit(2)
        
        return data
    
    
    
    def count_user():
        count = db.users.count_documents({})
        return count
    
    