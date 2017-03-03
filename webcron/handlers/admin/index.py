from tornado.web import authenticated
from webcron.handlers.base import BaseHandler


class IndexHandler(BaseHandler):
    # @authenticated
    def get(self, *args, **kwargs):
        self.render('admin/index.html', title='web cron admin')
