# -*- coding:utf-8 -*-
import json
from pony.orm import db_session
from webcron.db import User
from webcron.handlers.base import BaseHandler


class RegisterHandler(BaseHandler):

    def post(self, *args, **kwargs):
        body = json.loads(self.request.body)
        username = body.get('username')
        password = body.get('password')
        with db_session:
            if User.get(username=username) is not None:
                self.write('0')
                return
            User(username=username, password=User.hashpassword(password))
            self.write('1')
            return