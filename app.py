from flask import Flask
from flask_cors import CORS 
from resources.Users import users
from resources.Comments import comments
from resources.Accounts import accounts
app = Flask(__name__)
CORS(app)

app.register_blueprint(users)
app.register_blueprint(comments)
app.register_blueprint(accounts)

if __name__ =='__main__':
    app.run(debug = True, port= 5000)

