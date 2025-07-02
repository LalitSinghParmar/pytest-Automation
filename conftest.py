import pytest
from io import StringIO

@pytest.fixture
def fake_user():
    return {"username": "lalit", "role": "admin"}

@pytest.fixture
def mock_open(monkeypatch):
    def _mock_open(content):
        monkeypatch.setattr("builtins.open", lambda *args, **kwargs: StringIO(content))
    return _mock_open
