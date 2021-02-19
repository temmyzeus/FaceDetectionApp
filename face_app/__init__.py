from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "ba6fba9c2ea5397fa45dc6c41c5817aa"

from face_app import routes