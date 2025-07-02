import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from file_utils import config_exists

def test_config_file_exists(monkeypatch):
    monkeypatch.setattr("file_utils.os.path.exists", lambda path: True)
    assert config_exists() is True
