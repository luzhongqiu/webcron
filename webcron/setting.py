# -*- coding:utf-8 -*-
import os

WEB_SETTINGS = {
    "static_path": os.path.join(os.path.dirname(os.path.dirname(__file__)), "static"),
    "cookie_secret": "jfoirjgfeiorgjermgreopjgtreioghjeiorjg",
    "xsrf_cookies": False,
    'template_path': os.path.join(os.path.dirname(os.path.dirname(__file__)), "templates"),
    "gzip": True,
    "debug": True,
    "login_url": "/login"
}