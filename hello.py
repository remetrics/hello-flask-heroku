from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/')
def forward_request():
    #test
    return request.get_data() 

if __name__ == '__main__':
    app.run()
