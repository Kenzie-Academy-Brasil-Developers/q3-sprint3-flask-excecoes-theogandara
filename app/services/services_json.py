import json
import os
from flask import jsonify

DATABASE = os.getenv("FILEPATH")


def read_json():
    with open(DATABASE, "r") as database_file:

        return json.load(database_file)


def write_json(payload: dict):

    content = add_user(payload)

    initialize_database = {"data": content}

    if not os.path.isfile(DATABASE) or os.stat(DATABASE).st_size == 0:

        initialize_database2 = {"data": [payload]}

        with open(DATABASE, "w") as database_file:
            json.dump(initialize_database2, database_file)

    with open(DATABASE, "w") as database_file:

        json.dump(initialize_database, database_file, indent=4)


def checking_file_exists():
    initialize_database = {"data": []}

    if not os.path.isfile(DATABASE) or os.stat(DATABASE).st_size == 0:
        with open(DATABASE, "w") as database_file:
            json.dump(initialize_database, database_file)


def id_generator():

    if not os.path.isfile(DATABASE) or os.stat(DATABASE).st_size == 0:
        return 1

    users = read_json()["data"]

    if len(users) == 0:
        return 1

    last_id = int(len(users))
    last_user = users[last_id - 1]
    new_id = last_user["id"] + 1
    return new_id


def add_user(user: dict):
    if not os.path.isfile(DATABASE) or os.stat(DATABASE).st_size == 0:
        return [user]

    new_list = read_json()["data"]
    new_list.append(user)

    return new_list
