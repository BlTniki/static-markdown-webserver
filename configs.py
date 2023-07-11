import os


class Config(object):
    DEBUG = True
    SECRET_KEY = "you-will-never-guess"
    PATH_TO_VAULT = os.path.abspath(r"")
    OFFICIAL_EXTENSIONS_TO_USE = ['fenced_code', 'tables', 'nl2br']
    OFFICIAL_EXTENSIONS_CONFIG = {}
    CONFIG_MSG = "ABS!!"


class DevConfig(Config):
    DEBUG = os.environ.get("DEBUG") or True
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    PATH_TO_VAULT = os.environ.get("PATH_TO_VAULT") or os.path.abspath(r"app/md_static/")
    OFFICIAL_EXTENSIONS_TO_USE = os.environ.get("OFFICIAL_EXTENSIONS_TO_USE") or ['fenced_code', 'tables', 'nl2br']
    OFFICIAL_EXTENSIONS_CONFIG = os.environ.get("OFFICIAL_EXTENSIONS_TO_USE") or {}
    CONFIG_MSG = "DEV!!"


class ProdConfig(Config):
    DEBUG = os.environ.get("DEBUG") or False
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    PATH_TO_VAULT = os.environ.get("PATH_TO_VAULT") or os.path.abspath(r"app/md_static/")
    OFFICIAL_EXTENSIONS_TO_USE = os.environ.get("OFFICIAL_EXTENSIONS_TO_USE") or ['fenced_code', 'tables', 'nl2br']
    OFFICIAL_EXTENSIONS_CONFIG = os.environ.get("OFFICIAL_EXTENSIONS_TO_USE") or {}
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
