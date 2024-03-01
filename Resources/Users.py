from flask import jsonify, request, Blueprint
from models.User import User


users = Blueprint("users", __name__)

@users.route('/api/user', methods=['GET'])
def get_users():
    try:
        result = User.get_all_users()
        items=[]
        for user in result:
            item ={
                "_id":str(user["_id"]),
                "name":(user["name"]),
                "phone":(user["phone"]),
                "password":(user["password"])
            }
            
            items.append(item)
        
        return jsonify({
                "success": True,
                "data": items,
                "status":200
            }), 200
        
    except Exception as e:
         return jsonify({
            "message": str(e),
            "status": 500
        }), 500





@users.route('/api/user', methods=['POST'])
def add_user():
    try:
        body = request.get_json()
        print(body)
        if not body:
            return jsonify({
                "message": "Some data are missing",
                "error": "Missing DATA in request",
                "status":400
            }), 400
        
        name = body.get("name")
        phone = body.get("phone")
        password = body.get("password")
        # print(data)
        
        
        if not name or not phone or not password:
             return jsonify({
                "message": "Some data are missing",
                "error": "Missing Data are request",
                "status":400
            }), 400
        
        
        data = User(body)
      
        result = data.save_to_db()
        if result.acknowledged == True:
            return jsonify({
                "message": "User saved successfully",
                "success": True,
                "status": 201
            })
            
        return jsonify({
                "message": "Something went wrong",
                "success": False,
                "status":500
            }), 201
        
     
    except Exception as e:
        return jsonify({
            "message": str(e)
        }), 500
        

@users.route('/api/user/<string:id>', methods=['GET'])

def update_user_details(id):
    data = User.find_user(id)
    return jsonify("i am called and my id is {} and data is {}".format(id, data))


@users.route('/api/user/<string:id>', methods=["PUT"])
def update_user_info(id):
    try:
        payload = request.json
        if not payload:
            return jsonify({
                    "message": "Some data are missing",
                    "error": "Missing Data are request",
                    "status":400
                }), 400
        
        name = payload['name']
        print(name)
        phone = payload['phone']
        password = payload['password']
        
        data = User(payload)
        result = data.update_user_info(id)
        print(result)
        
        if result.acknowledged == True:
            return jsonify({
                    "message": "User successfully updated",
                    "success": True,
                    "status": 203
                }), 201
        
        return jsonify({
                    "message": "Something went wrong",
                    "success": False,
                    "status": 500
                }), 201
    
    except Exception as e:
        return jsonify({
            "message": str(e)
        }), 500