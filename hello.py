from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/')
def forward_request():
    #test
    return json.dumps(dict(request.headers))

if __name__ == '__main__':
    app.run()
