import requests

url = 'http://localhost:4000/api'

data = {}

result = requests.post(url, data=data)

print(result)
