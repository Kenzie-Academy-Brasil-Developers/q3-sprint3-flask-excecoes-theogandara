import os
from app.services.services_json import read_json

DATABASE = os.getenv("FILEPATH")


def email_already_exists(payload: dict):

    if not os.path.isfile(DATABASE) or os.stat(DATABASE).st_size == 0:
        return False

    users = read_json()["data"]

    email_to_be_verified = payload["email"]

    for user in users:
        if user["email"] == email_to_be_verified:
            return True

    return False
