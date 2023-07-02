from flask import Flask
from flask_commonmark import Commonmark
from flask_debugtoolbar import DebugToolbarExtension

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
cm = Commonmark(app)
toolbar = DebugToolbarExtension(app)

from app import routes