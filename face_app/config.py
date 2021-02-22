from face_app import app
import os

image_types_allowed = ["jpeg", "jpg", "png"]
images_download_path = os.path.join(app.root_path, "static", "images")