#!/usr/bin/env python3

from tornado import httpserver
from tornado import gen
from tornado.ioloop import IOLoop
import tornado.web
import sqlite3 as sqlite

from app.logs import logs
from rest.users import UsersHandler

logger = logs('server')

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        logger.debug("GET triggered")
        self.render("templates/home.html")
        #self.write('Welcome to OneLab test')

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/?", MainHandler),
            (r"/api/v1/users?", UsersHandler),
            (r"/api/v1/users/([A-Za-z0-9-]+)/?", UsersHandler)
        ]
        tornado.web.Application.__init__(self, handlers)

    def verifyDatabase(self):
        conn = sqlite.connect('db/users.db')
        c = conn.cursor()
        try:
            c.execute('SELECT * FROM users')
            print('Table already exists')
        except:
            print('Creating table \'users\'')
            c.execute('CREATE TABLE users (\
                id text,\
                first_name text,\
                last_name text,\
                password text)')
            print('Successfully created table \'users\'')
        conn.commit()
        conn.close()

def main():
    app = Application()
    # Verify the database exists and has the correct layout
    app.verifyDatabase()
    app.listen(8111)
    IOLoop.instance().start()

if __name__ == '__main__':
    main()
