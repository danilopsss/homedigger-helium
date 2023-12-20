import os

from flask import Flask
from .core.utils import load_local_config_to_app


app = Flask(__name__)
env = os.environ.get("ENV", "development")
local_configs = load_local_config_to_app(env)
app.config.update(local_configs)


# Register the blueprint with the app
# from .services.proxy.authservice.routes import proxy_bp

# app.register_blueprint(proxy_bp)


if __name__ == '__main__':
    app.run()
