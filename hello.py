from flask import Flask, request
import json
import pprint

class LoggingMiddleware(object):
    def __init__(self, app):
        self._app = app

    def __call__(self, environ, resp):
        errorlog = environ['wsgi.errors']
        pprint.pprint(('REQUEST', environ), stream=errorlog)

        def log_response(status, headers, *args):
            pprint.pprint(('RESPONSE', status, headers), stream=errorlog)
            return resp(status, headers, *args)

        return self._app(environ, log_response)

app = Flask(__name__)

if __name__ == '__main__':
    app.wsgi_app = LoggingMiddleware(app.wsgi_app)
    app.run()
