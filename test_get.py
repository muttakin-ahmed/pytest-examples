import requests

base_url = "https://jsonplaceholder.typicode.com/"

print("this is a test script to demo GET and POST in pytest")
try: 
    response = requests.get(base_url + '/todos/11')
    response.raise_for_status()

    print(response.status_code)
    print(response.text)

    new_row = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response_post = requests.post(base_url+'posts')
    response_post.raise_for_status()

    print(response_post.status_code)
    print(response_post.text)
except requests.exceptions as e:
    print(e)

with open("pytest_exmaple/response.txt", "w") as f:
    f.write(response.text)
    
