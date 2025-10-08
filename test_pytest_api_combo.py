import pytest
import requests
from jsonschema import validate

@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"

def test_get_postings(base_url):
    response = requests.get(f"{base_url}/posts/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_post_postings(base_url):
    # Create a new entry -->> POST request
    payload = {
        "title" : "greaaaat!",
        "body" : "not so great :(",
        "userId" : 22
    }
    res = requests.post(f"{base_url}/posts", json=payload)
    assert res.status_code == 201
    assert res.json()["title"] == "greaaaat!"
    #print(res.json()["userId"])

def test_update_postings(base_url):
    # Full entry update -->> PUT request
    payload = {
        "id": 2,
        "title": "this is the updated title",
        "body": "this is a updated body",
        "userId": 200
        }
    response = requests.put(f"{base_url}/posts/2", json=payload)
    assert response.status_code == 200
    assert response.json()["title"] == payload["title"]
    assert response.json()["body"] == payload["body"]
    assert response.json()["id"] == payload["id"]
    assert response.json()["userId"] == payload["userId"]

def test_patch_postings(base_url, payload_id = 1):
    # PATCH request -->> partial update of entry
    payload = {"title": "patched title"}
    response = requests.patch(f"{base_url}/posts/"+str(payload_id), json=payload)
    assert response.status_code == 200
    assert response.json()["title"] == payload["title"]

def test_delete_postings(base_url):
    # Delete an entry -->> DELETE request
    response = requests.delete(f"{base_url}/posts/1")
    assert response.status_code in [200, 204]

def test_validate_jsonschema(base_url, payload_id = 1):
    schema = {
  "type": "object",
  "properties": {"id": 
                 {"type": "number"},
                 "title": 
                 {"type": "string"},
                 "body": 
                 {"type": "string"},
                 "userId": 
                 {"type": "number"},
                 },
  "required": ["id"]
}
    response = requests.get(f"{base_url}/posts/"+str(payload_id))
    assert response.status_code == 200
    validate(instance=response.json(), schema=schema)

def test_response_header(base_url, payload_id = 2):
    response = requests.get(f"{base_url}/posts/" + str(payload_id))
    assert response.headers["Content-type"] == "application/json; charset=utf-8"
    assert "cloudflare" in response.headers["Server"].lower()
    assert "Date" in response.headers

def test_with_token():
    token = "Bearer my_secret_token"
    headers = {"Authorization": token}
    response = requests.get("https://reqres.in/api/users/2", headers=headers)
    assert response.status_code == 200