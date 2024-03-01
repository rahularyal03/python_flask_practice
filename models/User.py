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
    

        
     
     
     
     
     
     
     
     
     
     
     
     
    # def save_to_db(self):
        # db.user.update_one({
        #      {"name": self.name},
        #     {
        #         "$set": {
                    
        #             "name": self.name,
        #             "password": self.password,
        #             "phone": self.phone,
        #             "created_at": self.create_at,

        #         },
              
        #     },
        #     True
        # })




