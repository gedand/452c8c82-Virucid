import requests

BASE = "http://localhost:5000/"

# response = requests.post(BASE + 'upload/sanyi')
# print(response.json())


# response = requests.post(BASE + 'registration', data={'username':'sanyi',
#                                                       'password':'baa'})
# print(response.json())
# response = requests.post(BASE + 'login', data={'username':'sanyi',
#                                                       'password':'baa'})
# print(response.json())
#
response = requests.post(BASE + 'upload', data={'file':'sanyiq'})
print(response.json())

# response = requests.get(BASE + 'search/2/2021-01-10/2022-02-02')
# print(response.json())

# response = requests.post(BASE + 'delete', data = {'fileid': '1'})
# print(response.json())

response = requests.post(BASE + 'comment', data = {'fileid': '1', 'comment': 'de rusnya :*'})
print(response.json())