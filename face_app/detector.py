from face_app import app
from flask import url_for
from face_recognition import face_locations
from PIL import Image, ImageDraw
import numpy as np
import os

def detect_face(img):
    image = img
    image_draw = ImageDraw.Draw(image)
    image_array = np.array(image)
    for (top, right, bottom, left) in face_locations(image_array):
        image_draw.rectangle([left,bottom,right,top], outline=(0,255,0), width=3)
    return image
