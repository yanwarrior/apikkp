import requests as rqs

url_token = 'http://127.0.0.1:8000/api-token-auth/'
r = rqs.post(url_token, data={'username':'admin', 'password': '1234567qwe'})
print(r.text)