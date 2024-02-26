# -*- coding: utf-8 -*-
"""Google_vision

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jw5KbB3NdCQ96dH80Ig760rc-WzgAaHP
"""

import os, io
from draw_vertices import drawVertices
from google.cloud import vision_v1
from google.cloud.vision_v1 import types
import pandas as pd

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'GV_logo detection.json'
client = vision_v1.ImageAnnotatorClient()

file_name = 'only_logos.jpg'
image_folder = '/home/jas/Desktop/Google_Vision_LogoDetection/GV_LogoDetection/'
image_path = os.path.join(image_folder, file_name)
print(image_path)
with io.open(image_path, 'rb') as image_file:
    content = image_file.read()


image = vision_v1.types.Image(content=content)
response = client.logo_detection(image=image)
logos = response.logo_annotations

for logo in logos:
    print('Logo Description:', logo.description)
    print('Confidence Score:', logo.score)
    print('-'*50)
    vertices = logo.bounding_poly.vertices
    print('Vertices Values {0}'.format(vertices))
    drawVertices(content, vertices, logo.description)
