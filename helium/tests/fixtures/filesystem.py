import os
import pytest
import tempfile


@pytest.fixture
def some_file():
    file = tempfile.NamedTemporaryFile(suffix=".toml")
    yield file.name
