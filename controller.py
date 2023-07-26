from flask import Blueprint, jsonify

authorise = Blueprint("authorise", __name__)


@authorise.route("/", methods=["GET"])
def get_api_key():
    try:
        return jsonify({"API_KEY": "THIS_IS_THE_API_KEY"}), 200
    except Exception:
        return jsonify({"Error": "Internal server error"}), 500
