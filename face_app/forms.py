from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField
from face_app.config import image_types_allowed

class ImagesForm(FlaskForm):
    image = FileField(label="Upload Image Here",
                        validators=[FileRequired(),
                                    FileAllowed(image_types_allowed,
                                                f"Only {image_types_allowed} files are allowed!!")])
    submit = SubmitField("Detect Faces")