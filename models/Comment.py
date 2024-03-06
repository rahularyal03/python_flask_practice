from dbconnect import db 
from bson import ObjectId
from datetime import datetime

class Comment(object):
    def __init__(self, data):
        self.comment = data.get('comment', [{}])
        self.id = ObjectId(data.get('id'))
        self.created_at = str(datetime.utcnow())
        
    def save_to_db(self):
        result = db.all_comments.update_one(
            {"user_id": self.id},
            {
                "$push": {
                    "comments": {
                        "comment": self.comment,
                        "created_at": self.created_at
                    }
                },
                "$set": {"user_id": self.id}
            },
            upsert=True
        )
        return result
    
    @staticmethod
    def get_all_comments(id):
        data = db.all_comments.find({"_id": ObjectId(id)})
        return data
    
    
    
   
    
    
    