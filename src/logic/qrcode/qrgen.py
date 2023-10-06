"""
LabelPrinterPro - JS 2 PY bridge 
Copyright (c) 2023 LPP team
All rights reserved.

@Author Julien Sluganovic
@File qrgen.py


Python based QR code generator
Output: qrcode[gen_number, date, time].png
"""

""" 
Imports
"""

import os
import datetime
import qrcode
import argparse

"""
Parser setup
"""

parser = argparse.ArgumentParser(description='Text to write in QR code')
parser.add_argument('input', type=str, help='Text to write in QR code (string)')
parser.add_argument('req_number', type=str, help='Request number (string)')
args = parser.parse_args()

def generateQRCode(data, req_number):
    """
    Generate QR code
    """
    # Create qrcode directory if it does not exist
    if not os.path.exists('qrcode'):
        os.makedirs('qrcode')

    # Generate QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='purple', back_color='white')

    # Save QR code
    # str(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')) + 
    file_name = 'qrcode/LPPqr' + '_' +  req_number + '.png'
    img.save(file_name)

    # Return file name
    return print(file_name)

generateQRCode(args.input, args.req_number)