import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
import api

class MockResponse:
    def __init__(self):
        self.status_code = 200

    def json(self):
        return {"id": 123, "name": "Lalit"}

def test_fetch_user(monkeypatch):
    monkeypatch.setattr("api.requests.get", lambda url: MockResponse())
    result = api.fetch_user(123)
    assert result["name"] == "Lalit"
