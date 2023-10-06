"""
LabelPrinterPro - jsonAPI
Copyright (c) 2023 LPP team
All rights reserved.

@Author Julien Sluganovic
@File api.py
"""
from time import sleep
import os
import json
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import subprocess
import random
app = Flask(__name__)

CORS(app)

# Enable CORS
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

# Endpoint to process incoming JSON documents
@app.route('/process', methods=['POST'])
def process_json():
    """
    Process incoming JSON document
    """
    
    auth_header = request.headers.get('Authorization')
    if not auth_header or auth_header != 'Bearer mysecrettoken':
        response = {'status': 'error', 'message': 'Invalid authorization token'}
        return jsonify(response), 401

    
    try:
        data = request.get_json()
    except Exception as e:
        response = {f'status': 'error', 'message': 'Invalid JSON payload', 'debug': e}
        print(response)
        return jsonify(response), 400   

    

    # Write JSON data to file
    file_name = 'data.json'
    with open(file_name, 'w') as f:
        json.dump(data, f)

    # Return a response
    response = {'status': 'success from LPP API', 'message': 'JSON received!'}
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



@app.route('/gqrcode', methods=['POST'])
def generate_qrCode():
    """
    Generate QR Code
    """
    # Get JSON data
    data = request.get_json()

    # Get QR Code data
    qrCode_data = data["qrCode_data"]
    req_number = data["req_number"]

    # Generate QR Code
    subprocess.Popen(['python', '../qrcode/qrgen.py', qrCode_data, req_number])
    
    
    
    # Return response
    response = {'status': 'success', 'message': 'QR Code generated!', 'req_number': req_number}
    return response


@app.route('/uqrcode/<req_number>', methods=['GET'])
def upload_qrCode_fromReqNumber(req_number):
    """
    Upload QR Code from request number
    """
    print(req_number)
    qr_file = f'./qrcode/LPPqr_{req_number}.png'

    if not os.path.exists(qr_file):
        response = {'status': 'error', 'message': 'File not found'}
        return jsonify(response), 404

        
    # Return response
    response = {'status': 'success', 'message': 'QR Code was served', 'req_number': req_number}

    return send_file(qr_file, mimetype='image/png')



@app.route('/this', methods=['POST'])
def this():
    """
    Generate QR Code
    """
    
    # Get JSON data
    data = request.get_json()

    # Get QR Code data
    qrCode_data = data["qrCode_data"]
    req_number = data["req_number"]
    # qr_file = f'./qrcode/LPPqr_{req_number}.png'
    qr_file = r"C:\Users\JulienSluganovic\Desktop\stuff\LabelPrinterPro\src\logic\jsonApi\qrcode" + f'\LPPqr_{req_number}.png'

    # Generate QR Code
    subprocess.Popen(['python', '../qrcode/qrgen.py', qrCode_data, req_number])
    
    
    
    # Return response
    response = {'status': 'success', 'message': 'QR Code generated!', 'req_number': req_number, 'tryUpload': "True"}
    sleep(0.5)
    return response and send_file(qr_file, mimetype='image/png')




if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')