import pytest
from pathlib import Path

@pytest.fixture
def toml_path():
    pathiter = Path(__file__).parent.parent.rglob("*.toml")
    yield next(pathiter, None)
