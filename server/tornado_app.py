#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options, parse_command_line

from file_upload import app


define("port", default=8888, help="run on the given port", type=int)
define("", default=8888, help="run on the given port", type=int)


def main():
    parse_command_line()
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(options.port)
    print('Listening on http://0.0.0.0:%d' % options.port)
    IOLoop.instance().start()


if __name__ == '__main__':
    main()
