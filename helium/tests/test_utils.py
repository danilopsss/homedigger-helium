from gatekeeper.core.utils import load_config_from_file


def test_load_toml_by_path(toml_path):
    config = load_config_from_file(toml_path.as_posix())
    assert config is not None
    assert type(config) is dict
