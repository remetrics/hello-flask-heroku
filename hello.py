from flask import Flask, request
import json
import os

app = Flask(__name__)

@app.route('/')
def forward_request():
    return json.dumps(list(os.environ.keys()))

app = Flask(__name__)

if __name__ == '__main__':
    app.run()
