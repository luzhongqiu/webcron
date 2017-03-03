# -*- coding:utf-8 -*-
import hashlib
from pony.orm import *
from passlib.apps import custom_app_context

db = Database()
db.bind('sqlite', 'users.db', create_db=True)


# db.create_tables()

class User(db.Entity):
    username = Required(str)
    password = Required(str)

    @staticmethod
    def hashpassword(password):
        return custom_app_context.encrypt(password)

    def vertify_password(self, password):
        return custom_app_context.verify(password, self.password)


class Global(db.Entity):
    g_k = PrimaryKey(str)
    g_v = Required(str)


db.generate_mapping(create_tables=True)
