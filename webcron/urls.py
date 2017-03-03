# -*- coding: utf-8 -*-
from tornado.ioloop import IOLoop
from tornado.web import Application
from webcron.handlers import login
from webcron.handlers import register


def run(g):
    setting = g.pop('setting')
    application = Application([
        (r'/login(/?)', login.LoginHandler, dict(g=g)),
        (r'/register(/?)', register.RegisterHandler, dict(g=g)),
    ], **setting)
    print 'listening port {}'.format(g['port'])
    application.listen(int(g['port']))
    IOLoop.instance().start()
