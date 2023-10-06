import os
import argparse
import barcode
from barcode.writer import ImageWriter

def generate_barcode(barcode_number, req_number):
    """
    Generate barcode image and save to file
    """
    # Generate barcode string
    barcode_str = str(barcode_number)

    # Generate barcode image
    barcode_img = barcode.Code128(barcode_str, writer=ImageWriter())

    # Save barcode image
    file_name = f"bCode_{barcode_number}.png"
    file_storage = f"data/req/{req_number}/barcode/{file_name}"
    with open(file_storage, 'wb') as f:
        barcode_img.write(f)

    # Return file name
    return file_name

def read_barcode(file_name):
    """
    Read barcode image from file
    """
    # Read barcode image
    file_path = f"data/barcode/{file_name}"
    with open(file_path, 'rb') as f:
        barcode_img = f.read()

    # Return barcode image
    return barcode_img

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Generate and read barcodes')
    parser.add_argument('mode', choices=['generate', 'read'], help='Mode of operation')
    parser.add_argument('--barcode-number', type=int, help='Barcode number')
    parser.add_argument('--req-number', type=int, help='Request number')
    parser.add_argument('--file-name', help='Barcode image file name')
    args = parser.parse_args()

    if args.mode == 'generate':
        # Generate barcode image
        barcode_number = args.barcode_number
        req_number = args.req_number
        file_name = generate_barcode(barcode_number, req_number)
        print(f"Barcode image generated: {file_name}")
    elif args.mode == 'read':
        # Read barcode image
        file_name = args.file_name
        barcode_img = read_barcode(file_name)
        print(f"Barcode image read: {file_name}")