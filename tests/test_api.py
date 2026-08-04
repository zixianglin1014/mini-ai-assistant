import requests

url = "http://127.0.0.1:8000/api/chat"


data = {"message": "介绍一下人工智能"}


response = requests.post(url, json=data)


print(response.json())
