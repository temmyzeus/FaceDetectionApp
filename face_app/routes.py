from face_app import app
from flask import render_template, url_for, request, flash
from face_app.forms import ImagesForm
from PIL import Image
import secrets
import os
from face_app.detector import detect_face

def save_image(form_image):
    """Saves Image to Specified Path"""
    random_filename = str(secrets.token_urlsafe(16))
    ext = os.path.splitext(form_image.filename)[-1]
    root_path = app.root_path
    filename = random_filename + ext
    save_path = os.path.join(root_path, "static", "images", filename)
    image = Image.open(form_image)
    image = detect_face(img= image)
    image.save(save_path)
    return filename

@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    form = ImagesForm() # Form Object to Upload Images

    # This if-else clause doent seem to run even if form is submitted
    if request.method == "POST":
        image_filename = save_image(form.image.data)
        print(image_filename)
        return render_template("index.html", title="Detect Faces", form=form, image_filename=image_filename)

    return render_template("index.html", title="HomePage", form=form)