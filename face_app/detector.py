from face_app import app
from flask import url_for
from face_recognition import face_locations
from PIL import Image, ImageDraw
import numpy as np
import os

def fetch_image(filename: str):
    """
    Fetch image files with filename given

    @param: filename: File name of Image to fetch [str]
    """
    image_pth = os.path.join(app.root_path, "static", "images", filename)
    return Image.open(image_pth)

def detect_face(img):
    global image_array
    image = img
    image_draw = ImageDraw.Draw(image)
    image_array = np.array(image)
    for (top, right, bottom, left) in face_locations(image_array):
        image_draw.rectangle([left,bottom,right,top], outline=(0,255,0), width=3)
    return image
