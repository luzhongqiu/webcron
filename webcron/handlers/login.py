# -*- coding:utf-8 -*-
import json
from pony.orm import db_session
from webcron.db import User
from webcron.handlers.base import BaseHandler


class LoginHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('login.html', title='web cron')

    def post(self, *args, **kwargs):
        body = json.loads(self.request.body)
        username = body.get('username')
        password = body.get('password')

        if self._login(username, password):
            return_data = {
                'status': 1,
                'error': ''
            }
        else:
            return_data = {
                'status': 0,
                'error': 'username or password wrong!'
            }
        self.write(json.dumps(return_data))

    #
    def _login(self, username, password):
        with db_session:
            user = User.get(username=username)
            if user is not None:
                if user.vertify_password(password):
                    return True
            return False
