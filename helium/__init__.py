import os

from flask import Flask
from .core.utils import load_local_config_to_app


app = Flask(__name__)
env = os.environ.get("ENV", "development")
local_configs = load_local_config_to_app(env)
app.config.update(local_configs)


# Register the blueprint with the app
from .services.authservice.routes import auth_bp

app.register_blueprint(auth_bp, url_prefix="/api/v1/auth")


if __name__ == "__main__":
    app.run()
