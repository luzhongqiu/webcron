# -*- coding:utf-8 -*-
import logging
from tornado.web import RequestHandler


class BaseHandler(RequestHandler):

    def initialize(self, g):
        self.logger = logging.getLogger(g.get('logger'))
        self.logger.info('access log: {}'.format(self.request))
        self.global_config = g