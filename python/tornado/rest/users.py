#!/usr/bin/env python3

import tornado.web

class UsersHandler(tornado.web.RequestHandler):

    def get(self, id=None):
        if id:
            self.write("GET - user with id %s" % id)
        else:
            self.write('GET - all users')

    def post(self):
        # [{
        # "id":1,
        # "first_name":"John",
        # "last_name":"Doe",
        # "password":"xy"
        # }]
        self.write('POST - a new user')

    def put(self, id):
        self.write('PUT - user with id %s' % id)

    def delete(self, id):
        self.write('DELETE - user with id %s' % id)
