from http import HTTPStatus
import os
from flask import Flask, request

from app.models.user_model import User

from app.services import checking_file_exists
from app.services.services_json import id_generator, write_json
from app.services.services_user import email_already_exists

app = Flask(__name__)


@app.get("/user")
def retrieve():
    checking_file_exists()
    return User.get_users(), HTTPStatus.OK


@app.post("/user")
def return_post():
    data = request.get_json()

    if email_already_exists(data):
        error_message = {"error": "User already exists."}
        return error_message, HTTPStatus.CONFLICT

    data.update({"id": id_generator()})

    write_json(data)

    result = {"data": data}

    return result, HTTPStatus.CREATED
