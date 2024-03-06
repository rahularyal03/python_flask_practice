from flask import Flask, Blueprint,  jsonify, request, json
from models.Account import Account

accounts = Blueprint("accounts", __name__)

@accounts.route("/bank/add_account", methods=['POST'])
def add_account_to_db():
    payload = request.json
    print(payload)
    # holder = payload.get("holder")
    # id = payload.get("id")
    # type = payload.get("type")
    # balance = payload.get("balance")
    # tranfer_completed = payload.get("transfer_completed")
    
    data = Account(payload)
    result = data.add_account()
    print(result)
    return jsonify({"message": "Successfully created"}), 201


@accounts.route("/bank/add_account", methods = ['GET'])
def get_user_info():
    result = Account.get_info()
    item = []
    for i in result:
        i["_id"] = str(i["_id"])
        item.append(i)
        
    return jsonify({"data": item}), 200
