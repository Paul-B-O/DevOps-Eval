import pytest

from app import app

def test_database_is_connected():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.get_data(as_text=True) == "Database Connection Status: Connected"