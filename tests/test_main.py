"""
tests.py

"""

import pytest
import os
from fastapi.testclient import TestClient
from api import app
env = os.environ

def test_main_root():
    with TestClient(app) as client:
        response = client.get(env["BASE_PATH"])
        assert response.status_code == 200

def test_sub_root():
    with TestClient(app) as client:
        response = client.get(env["SUB_PATH"])
        assert response.status_code == 200
