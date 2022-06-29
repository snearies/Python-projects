import sys
import os
from PIL import Image
input_image = sys.argv[1] if len(sys.argv) > 1 else '.'
output_image = sys.argv[2] if len(sys.argv) > 1 else '.'

if not os.path.exists(output_image):
    os.makedirs(output_image)
    for filename in os.listdir(input_image):
        img = Image.open(f'{input_image}{filename}')
        clean_name = os.path.splitext(filename)[0]
        img.save(f'{output_image}{clean_name}.png','png')






















