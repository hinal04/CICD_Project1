import threading
import time
import requests
import pytest
from app import Handler
from http.server import HTTPServer


@pytest.fixture(scope="module")
def server():
    httpd = HTTPServer(("localhost", 8001), Handler)
    thread = threading.Thread(target=httpd.serve_forever)
    thread.daemon = True
    thread.start()
    time.sleep(1)
    yield
    httpd.shutdown()


def test_health_returns_200(server):
    response = requests.get("http://localhost:8001/health")
    assert response.status_code == 200


def test_health_returns_ok(server):
    response = requests.get("http://localhost:8001/health")
    assert response.text == "OK"


def test_unknown_path_returns_404(server):
    response = requests.get("http://localhost:8001/unknown")
    assert response.status_code == 404
