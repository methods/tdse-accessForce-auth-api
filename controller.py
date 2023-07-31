from flask import Blueprint, jsonify, request
import jwt
import datetime


authorise = Blueprint("authorise", __name__)


@authorise.route("/", methods=["GET"])
def get_api_key():
    try:
        return jsonify({"API_KEY": "THIS_IS_THE_API_KEY"}), 200
    except Exception as e:
        return jsonify({"Error": str(e)}), 500


@authorise.route("/", methods=["POST"])
def get_jwt():
    try:
        secret = "THIS_IS_A_SECRET"
        payload = request.json
        if payload["username"] in admin_users:
            payload["admin"] = True
        else:
            payload["admin"] = False
        payload["exp"] = datetime.datetime.utcnow() + datetime.timedelta(seconds=60)
        token = jwt.encode(payload=payload, key=secret)
        return jsonify({"jwt": token}), 200
    except Exception as e:
        return jsonify({"Error": str(e)}), 500


admin_users = ["Julio", "Pira", "Nathan"]
