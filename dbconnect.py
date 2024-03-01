import os
from pymongo import MongoClient

db = MongoClient(os.getenv("MONGODB_URI"),
                 authSource='admin',
                 maxPoolSize=50,
                 wtimeoutMS=2500)["Flask_test"]