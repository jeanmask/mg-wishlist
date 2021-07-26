import json

import pytest

DEFAULT_HEADERS = {"HTTP_AUTHORIZATION": "Bearer supersecret"}


@pytest.mark.django_db
def test_customer_list(client, customers_objs):
    response = client.get("/customers/", **DEFAULT_HEADERS)
    response_data = response.json()

    assert response.status_code == 200
    assert len(response_data) == len(customers_objs)

    for c in customers_objs:
        assert {"id": str(c.id), "name": c.name, "email": c.email} in response_data


@pytest.mark.django_db
def test_customer_get(client, customers_objs):
    for c in customers_objs:
        response = client.get(f"/customers/{c.id}", **DEFAULT_HEADERS)
        response_data = response.json()

        assert response.status_code == 200
        assert {"id": str(c.id), "name": c.name, "email": c.email} == response_data


@pytest.mark.django_db
def test_customer_post(client, customers):
    for c in customers:
        response = client.post(
            "/customers/", json.dumps(c), content_type="application/json", **DEFAULT_HEADERS
        )
        assert response.status_code == 201
        response_data = response.json()
        assert response_data["id"]
        assert response_data["name"] == c["name"]
        assert response_data["email"] == c["email"]


@pytest.mark.django_db
def test_customer_post_duplicate_email(client, customer):
    response = client.post(
        "/customers/", json.dumps(customer), content_type="application/json", **DEFAULT_HEADERS
    )
    assert response.status_code == 201

    customer["name"] = "Some new name :P"
    response = client.post(
        "/customers/", json.dumps(customer), content_type="application/json", **DEFAULT_HEADERS
    )
    assert response.status_code == 422

    response_data = response.json()
    assert response_data["detail"] == "Customer e-mail already exists"


@pytest.mark.django_db
def test_customer_put(client, customers_objs):
    for ix, c in enumerate(customers_objs):
        data = {"name": f"Edited name {ix}", "email": f"edited_email_{ix}@something.com"}
        response = client.put(
            f"/customers/{c.id}", json.dumps(data), content_type="application/json", **DEFAULT_HEADERS
        )
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["id"]
        assert response_data["name"] == data["name"]
        assert response_data["email"] == data["email"]


@pytest.mark.django_db
def test_customer_put_duplicate_email(client, customers_objs):
    c = customers_objs[0]
    used_email = customers_objs[1].email

    response = client.put(
        f"/customers/{c.id}",
        json.dumps({"name": c.name, "email": used_email}),
        content_type="application/json",
        **DEFAULT_HEADERS,
    )
    assert response.status_code == 422

    response_data = response.json()
    assert response_data["detail"] == "Customer e-mail already exists"


@pytest.mark.django_db
def test_customer_delete(client, customers_objs):
    for ix, c in enumerate(customers_objs):
        data = {"name": f"Edited name {ix}", "email": f"edited_email_{ix}@something.com"}

        response = client.put(
            f"/customers/{c.id}", json.dumps(data), content_type="application/json", **DEFAULT_HEADERS
        )

        assert response.status_code == 200

        response_data = response.json()
        assert response_data["id"]
        assert response_data["name"] == data["name"]
        assert response_data["email"] == data["email"]
