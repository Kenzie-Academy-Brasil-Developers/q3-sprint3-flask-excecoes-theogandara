import os

from app.services import read_json
from app.services import write_json


class User:

    DATABASE_FILEPATH = os.getenv("FILEPATH")

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    @classmethod
    def get_users(cls):
        return read_json()

    def add_user(self):
        return write_json(self.__dict__)
