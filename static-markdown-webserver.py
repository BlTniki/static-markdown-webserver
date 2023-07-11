from configs import ProdConfig, ConfigHandler
ConfigHandler.set_config(ProdConfig())

from app.main import app

if __name__ == "__main__":
    app.run(debug=ConfigHandler.get_config().DEBUG, use_reloader=False)
