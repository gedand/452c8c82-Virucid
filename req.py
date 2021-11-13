import requests

BASE = "http://localhost:5000/"

response = requests.post(BASE + 'upload/sanyi')
print(response.json())
# response = requests.post(BASE + 'upload/sanyik')
# print(response.json())
response = requests.get(BASE + 'search/2/2021-01-10/2022-02-02')
print(response.json())
# response = requests.post(BASE + 'registration/sanyi/baa')
# print(response.json())
# response = requests.post(BASE + 'login/sanyi/baa')
# print(response.json())