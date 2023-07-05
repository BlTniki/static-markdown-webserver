from configs import DevConfig, ConfigHandler

if __name__ == "__main__":
    ConfigHandler.set_config(DevConfig())

    from app.main import app

    app.run(debug=ConfigHandler.get_config().DEBUG, use_reloader=False)
