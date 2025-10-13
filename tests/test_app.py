from app import app


def test_home_route():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b"Hello, Flask!" in response.data


def test_health_check():
    tester = app.test_client()
    response = tester.get('/health')
    assert response.status_code == 200
    assert response.json == {"status": "ok"}
