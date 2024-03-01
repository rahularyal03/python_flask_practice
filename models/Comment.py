from dbconnect import db 
from bson import ObjectId
from datetime import datetime

class Comment(object):
    def __init__(self, data):
        self.comment = data.get('comment', [])
        self.id = ObjectId(data.get('id'))
        
    
    def save_to_db(self):
        data = db.comments.insert_one(
            {
                "comment": [self.comment],
                "user_id": self.id
            }
        )
        
        return data
