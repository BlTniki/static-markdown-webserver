from configs import ConfigHandler
from app.filesystem_accounter import FilesystemAccounter

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
import os
import logging
from logging.handlers import RotatingFileHandler

print(ConfigHandler.get_config().CONFIG_MSG)

app = Flask(__name__)
app.config.from_object(ConfigHandler.get_config())


if app.config["DEBUG"]:
    toolbar = DebugToolbarExtension(app)

if not os.path.exists('logs'):
    os.mkdir('logs')

# setup rotating INFO logging
file_handler = RotatingFileHandler('logs/info.log', maxBytes=10240,
                                   backupCount=10)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)

app.logger.setLevel(logging.INFO)
app.logger.info('App startup')

# setup rotating ERROR logging
file_handler = RotatingFileHandler('logs/error.log', maxBytes=10240,
                                   backupCount=10)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
file_handler.setLevel(logging.ERROR)
app.logger.addHandler(file_handler)

app.logger.setLevel(logging.ERROR)

# Setup filetree accounter
dirtree_accounter = FilesystemAccounter(ConfigHandler.get_config())

from app.main import error_handler, routes
