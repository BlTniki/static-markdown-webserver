import os


class Config(object):
    DEBUG = os.environ.get("DEBUG") or True
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    PATH_TO_VAULT = os.environ.get("PATH_TO_VAULT") or os.path.abspath(r"app/md_static/")
    OFFICIAL_EXTENSIONS_TO_USE = os.environ.get("OFFICIAL_EXTENSIONS_TO_USE") or ['fenced_code', 'tables', 'nl2br']
    OFFICIAL_EXTENSIONS_CONFIG = os.environ.get("OFFICIAL_EXTENSIONS_TO_USE") or {}
