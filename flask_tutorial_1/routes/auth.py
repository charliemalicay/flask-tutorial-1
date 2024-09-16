from flask import Blueprint, jsonify, request
from werkzeug.security import check_password_hash

import jwt

from flask_tutorial_1.routes import allowed_users

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    d = request.json

    if "username" not in d or "password" not in d:
        raise Exception("Unable to authenticate")

    if not check_password_hash(
        allowed_users[d["username"]],
        d["password"]
    ):
        raise Exception("Invalid password")

    encoded_jwt = jwt.encode(
        { "sub": 1, "name": "sergio" },
        "mysecret",
        algorithm="HS256"
    )

    return jsonify({ "token": encoded_jwt })
