"""
Barcode generater in Python
Output: barcode[gen_number, date, time].png

"""


"""
Imports
"""
import datetime
import cv2
from pyzbar.pyzbar import decode

import barcode
from barcode.writer import ImageWriter

import json

def generate_barcode(barcode_number):
    """
    Generate barcode image from barcode number
    
    """

    # Generate date and time
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    time = datetime.datetime.now().strftime("%H:%M:%S")

    # Generate barcode
    barcode_str = str(barcode_number) + ", " + str(date) + ", " + str(time)

    # Generate barcode image
    barcode_img = barcode.Code128(barcode_str, writer=ImageWriter())

    # Save barcode image
    # file_name = "barcode[" + str(barcode_number) + "_" + str(date) + "_" + str(time) + "].png"
    file_name = f"barcode_{barcode_number}.png"
    file_storage = f"data/req/{req_number}/barcode/{file_name}"
    with open(file_storage, 'wb') as f:
        barcode_img.write(f)

    # Return file name
    return file_name

def read_barcode(file_name):
    """
    Read barcode from image file
    """
    
    # Load image file
    img = cv2.imread(file_name)

    # Decode barcode
    barcode = decode(img)

    # Return barcode data
    return barcode[0].data.decode('utf-8')


def read_barcodeNumber(file_path):
    """
    Read barcode from image file
    """
    # load json file 
    with open(file_path, 'r') as f:
        data = json.load(f)
    # Get barcode number
    barcode_number = data["barcode_number"]
    # Return barcode number
    return barcode_number

def read_reqNumber(file_path):
    """
    Read barcode from image file
    """
    # load json file 
    with open(file_path, 'r') as f:
        data = json.load(f)
    # Get barcode number
    req_number = data["req_number"]
    # Return barcode number
    return req_number

# Example usage
barcode_number = read_barcodeNumber(f"data/req/{str(read_reqNumber())}/barcode.json")
file_name = generate_barcode(barcode_number)
print("Generated barcode image:", file_name)


# barcode_data = read_barcode(file_name)
# print("Read barcode data:", barcode_data)