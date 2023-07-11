import os
import json


class Config(object):
    DEBUG = True
    SECRET_KEY = "you-will-never-guess"
    PATH_TO_VAULT = os.path.abspath(r"")
    OFFICIAL_EXTENSIONS_TO_USE = ['fenced_code', 'tables', 'nl2br']
    OFFICIAL_EXTENSIONS_CONFIG = {}
    CONFIG_MSG = "ABS!!"


class ProdConfig(Config):
    DEBUG = os.environ.get("DEBUG") == "True"
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    PATH_TO_VAULT = os.environ.get("PATH_TO_VAULT") or os.path.abspath(r"app/md_static/")
    OFFICIAL_EXTENSIONS_TO_USE = json.loads(os.environ.get("OFFICIAL_EXTENSIONS_TO_USE")) if os.environ.get(
        "OFFICIAL_EXTENSIONS_TO_USE") else ['fenced_code', 'tables', 'nl2br']
    OFFICIAL_EXTENSIONS_CONFIG = json.loads(os.environ.get("OFFICIAL_EXTENSIONS_CONFIG")) if os.environ.get(
        "OFFICIAL_EXTENSIONS_CONFIG") else {}
    CONFIG_MSG = "PROD!!"


class TestConfig(Config):
    DEBUG = True
    SECRET_KEY = "you-will-never-guess"
    PATH_TO_VAULT = os.path.abspath(r"")
    OFFICIAL_EXTENSIONS_TO_USE = ['fenced_code', 'tables', 'nl2br']
    OFFICIAL_EXTENSIONS_CONFIG = {}
    CONFIG_MSG = "TEST!!"

class ConfigHandler:
    _config = Config()  # Default config

    @staticmethod
    def set_config(config: Config):
        ConfigHandler._config = config

    @staticmethod
    def get_config():
        return ConfigHandler._config
