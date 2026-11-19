import requests
try:
    response=requests.get("https://jsonplaceholder.typicode.com/posts/1",timeout=10)
    response.raise_for_status()
    data=response.json()
    print("data status code:",response.status_code)
    print("API data:",data)
    print("title:",data["title"])
except requests.exceptions.RequestException as e:
    print("error:",e)