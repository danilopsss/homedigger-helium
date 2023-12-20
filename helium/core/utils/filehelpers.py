import tomllib


def load_config_from_file(file: str, env: str) -> dict:
    with open(file, "rb") as f:
        file = tomllib.load(f)
    compiled_config = {}
    for key, value in file.items():
        if key == env:
            compiled_config.update(value)
    return compiled_config
