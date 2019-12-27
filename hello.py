from flask import Flask, request
import json
import os

app = Flask(__name__)

@app.route('/')
def forward_request(self):
    return repr(self.environ)

if __name__ == '__main__':
    app.run()
