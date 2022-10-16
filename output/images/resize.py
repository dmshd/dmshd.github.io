"""
Resize an image keeping the aspect ratio
taking only a width as parameter
then convert it to webp (quality 60)
and save it in the same folder.
"""

import os
import sys
from PIL import Image

def resize_image(image_path, width):
    image = Image.open(image_path)
    height = int(width * image.size[1] / image.size[0])
    resized_image = image.resize((width, height), Image.ANTIALIAS)
    resized_image.save(image_path, optimize=True, quality=100)

def convert_image_to_webp(image_path):
    image = Image.open(image_path)
    image.save(image_path + '.webp', 'WEBP', quality=60)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python resize.py image_path width')
        sys.exit(1)
    image_path = sys.argv[1]
    width = int(sys.argv[2])
    resize_image(image_path, width)
    convert_image_to_webp(image_path)
