"""
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
parser = argparse.ArgumentParser(description='Text to write in QR code')
parser.add_argument('input', type=str, help='Text to write in QR code (string)')
args = parser.parse_args()

def generateQRCode(data):
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
    img = qr.make_image(fill='black', back_color='white')

    # Save QR code
    file_name = 'qrcode/qrcode' + str(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')) + '.png'
    img.save(file_name)

    # Return file name
    return file_name

generateQRCode(args.input)