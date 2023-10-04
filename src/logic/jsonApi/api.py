"""
LabelPrinterPro - jsonAPI
Copyright (c) 2023 LPP team
All rights reserved.

@Author Julien Sluganovic
@File api.py
"""

import os
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint to process incoming JSON documents
@app.route('/process', methods=['POST'])
def process_json():
    """
    Process incoming JSON document
    """
    data = request.get_json()

    # Write JSON data to file
    file_name = 'data.json'
    with open(file_name, 'w') as f:
        json.dump(data, f)

    # Return a response
    response = {'status': 'success'}
    return jsonify(response)

# Endpoint to retrieve a list of all saved JSON documents
@app.route('/list', methods=['GET'])
def list_json():
    """
    List all saved JSON documents
    """
    file_names = os.listdir('.')
    json_files = [f for f in file_names if f.endswith('.json')]

    data = []
    for file_name in json_files:
        with open(file_name, 'r') as f:
            data.append(json.load(f))

    # Return a response
    response = {'data': data}
    return jsonify(response)

# Endpoint to retrieve a specific JSON document by name
@app.route('/get/<name>', methods=['GET'])
def get_json(name):
    """
    Get a specific JSON document by name
    """
    file_name = name + '.json'

    if not os.path.exists(file_name):
        response = {'status': 'error', 'message': 'File not found'}
        return jsonify(response), 404

    with open(file_name, 'r') as f:
        data = json.load(f)

    # Return a response
    response = {'data': data}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)