#!/usr/bin/env python
"""
QR Code Generator
A simple Python program to generate QR codes from URLs.

Requirements:
- Install the qrcode library: pip install qrcode[pil]

Usage:
- Run the script: python qr_generator.py
- Enter a URL when prompted, or provide it as a command line argument
- The QR code will be saved as 'qrcode.png' in the current directory
"""

import qrcode
import sys

def generate_qr_code(url, filename='qrcode.png'):
    """
    Generate a QR code image from a URL.

    Args:
        url (str): The URL to encode in the QR code
        filename (str): The filename to save the QR code image (default: 'qrcode.png')
    """
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data to QR code
    qr.add_data(url)
    qr.make(fit=True)

    # Create and save the image
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print("QR code saved as {}".format(filename))

def main():
    # Check if URL is provided as command line argument
    if len(sys.argv) > 1:
        url = sys.argv[1]
        print("Generating QR code for: {}".format(url))
    else:
        # Prompt user for URL
        url = raw_input("Enter the URL to convert to QR code: ").strip()

    if not url:
        print("Error: No URL provided.")
        sys.exit(1)

    # Validate URL format (basic check)
    if not (url.startswith('http://') or url.startswith('https://')):
        print("Warning: URL should start with http:// or https://")

    # Generate QR code
    generate_qr_code(url)

if __name__ == "__main__":
    main()