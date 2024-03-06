from dbconnect import db
from datetime import datetime
from bson import ObjectId

class Account(object):
    def __init__(self, data):
        self.holder = data.get("holder")
        self.account_id = data.get("id")
        self.account_type = data.get("type")
        self.balance = data.get("balance")
        self.transfer_completed = data.get("transfer_completed", [])
        self.created_at = str(datetime.utcnow())
        
    
    def add_account(self):
        data = db.accounts.insert_one({
            "Account Id": self.account_id,
            "Account Holder": self.holder,
            "Account Type": self.account_type,
            "balance" : self.balance,
            "Transfer_Completed": self.transfer_completed,
            "created_at": self.created_at
            
        })
        
        return data
    
    
    def get_info():
        data = db.accounts.aggregate([
            
            # also we can use  $project to create and modify the document and 1 and 0 is used to display or hide the elements from the document 
            
           {
                "$match": {"Account Type":"saving"}
           }, 
           {
               "$group": {"_id": "$balance",
                          "total_count": {
                              "$count": {}
                          }
                
                          }
           },
           {
               "$set": {
                   "amount": 2000
                   }
            },
           {
               "$out": {
                   "db": "Flask_test",
                   "coll": "account_info"
               }
           }
           
        ])
        return data
    
        
    # $out will create or update the collection with the new data obtained from the above functions 