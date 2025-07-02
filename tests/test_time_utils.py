import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from time_utils import get_greeting
from datetime import datetime

class MockDatetime(datetime):
    @classmethod
    def now(cls):
        return cls(2023, 1, 1, 18, 30, 0)

def test_evening_greeting(monkeypatch):
    monkeypatch.setattr("time_utils.datetime", MockDatetime)
    assert get_greeting() == "Good evening"
