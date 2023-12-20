from pathlib import Path
from helium.core.utils import load_config_from_file


def load_local_config_to_app(env: str):
    local_configs = {}
    config_file = Path(__file__).parent.parent.rglob(f"*.toml")
    for file_found in config_file:
        local_configs.update(
            load_config_from_file(file_found, env)
        )
    return local_configs
