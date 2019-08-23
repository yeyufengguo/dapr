import flask
from flask import request, jsonify
from flask_cors import CORS
import json
import sys

app = flask.Flask(__name__)
CORS(app)

@app.route('/actions/subscribe', methods=['GET'])
def subscribe():
    return jsonify(['A','C'])

@app.route('/A', methods=['POST'])
def a_subscriber():
    content = request.json
    print(f'Topic A: {content}', file=sys.stderr)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

@app.route('/C', methods=['POST'])
def b_subscriber():
    content = request.json
    print(f'Topic C: {content}', file=sys.stderr)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

app.run()