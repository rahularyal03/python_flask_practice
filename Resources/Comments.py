from flask import  Flask, Blueprint, json, jsonify, request
from models.Comment import Comment
from models.User import User

comments = Blueprint("comments", __name__)

@comments.route('/api/comments', methods=['POST'])
def add_to_db():
    payload = request.json
    data = User(payload)
    isUserExist = data.find_user(payload)
    
    data = Comment(payload)
    result = data.save_to_db()
    
    if result.acknowledged == True:
        return jsonify({
            "message": "Your commment is posted",
            "success": True,
            "status": 201
        })
    
    return jsonify({
        "message": "Some Internal Error Occured",
        "success": True,
        "status": 500,
    })
    
    # currently working on it 