from flask import Blueprint, jsonify
import jwt
import datetime

authorise = Blueprint("authorise", __name__)

# Replace "THIS_IS_THE_API_KEY"with your actual secret key
SECRET_KEY = "THIS_IS_THE_API_KEY"

# Function to generate JWT token
def generate_token(user_info):
    payload = {
        "user_info": user_info,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1)  # Token expires in 1 day
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

# Updated route to return JWT token
@authorise.route("/", methods=["GET"])
def get_jwt_token():
    try:
        user_info = {
            "user_id": 123,
            "scope": "write"  # Add user's scope/permission information here
        }
        token = generate_token(user_info)
        return jsonify({"token": token}), 200
    except Exception:
        return jsonify({"Error": "Internal server error"}), 500