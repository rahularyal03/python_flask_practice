from flask import Flask, render_template, jsonify
from flask_cors import CORS 
from Resources.Users import users
from Resources.Comments import comments
app = Flask(__name__)
CORS(app)

app.register_blueprint(users)
app.register_blueprint(comments)

if __name__ =='__main__':
    app.run(debug = True, port= 5000)

