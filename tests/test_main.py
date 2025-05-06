from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello CI/CD"}


def test_read_product():
    response = client.get("/product/1")
    assert response.status_code == 200
    assert response.json() == {"product_id": 1, "name": "Product 1", "price": 25.99}


def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong"}


def test_create_product():
    response = client.post("/product/", json={"name": "New Product", "price": 19.99})
    assert response.status_code == 200
    assert response.json() == {
        "message": "Product created",
        "product": {"name": "New Product", "price": 19.99},
    }


def test_update_product():
    response = client.put(
        "/product/1", json={"name": "Updated Product", "price": 29.99}
    )
    assert response.status_code == 200
    assert response.json() == {
        "message": "Product 1 updated",
        "product": {"name": "Updated Product", "price": 29.99},
    }


def test_delete_product():
    response = client.delete("/product/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Product 1 deleted"}
