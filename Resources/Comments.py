from flask import  Flask, Blueprint, json, jsonify, request
from models.Comment import Comment
from models.User import User

comments = Blueprint("comments", __name__)

@comments.route('/api/comments', methods=['POST'])
def add_to_db():
    payload = request.json
    print(payload)
    
    data = Comment(payload)
    result = data.save_to_db()
    print(result)
    if result.acknowledged == True:
        return jsonify({
            "message": "Your commment is posted",
            "success": True,
            "status": 201
        }), 201
    
    return jsonify({
        "message": "Some Internal Error Occured",
        "success": True,
        "status": 500,
    }), 500
    
    
@comments.route('/api/comments/<string:id>', methods=['GET'])
def get_comment(id):
    try:
        result = Comment.get_all_comments(id)
        data = list(result)
        items=[]
        for comment in data:
            comment["_id"] = str(comment["_id"])
            comment["user_id"] = str(comment["user_id"])
            items.append(comment)
        return jsonify({"data": items})
        
    except Exception as e:
         return jsonify({
            "message": str(e),
            "status": 500
        }), 500
         
    
    
    



