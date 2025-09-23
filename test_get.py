import requests

base_url = "https://jsonplaceholder.typicode.com/"

print("this is a test script to demo GET and POST in pytest")
try: 
    response = requests.get(base_url + '/todos/')
    response.raise_for_status()

    print(response.status_code)
    print(response.text)

    new_row = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    res_post = requests.post(base_url+'posts')
    res_post.raise_for_status()

    print(res_post.status_code)
    print(res_post.text)
except requests.exceptions as e:
    print(e)

with open("response.txt", "w") as f:
    f.write(response.text)
    
