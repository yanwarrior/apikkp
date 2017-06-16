# Token f7641f4d0aecb6915a2bff70541ef4ecacc4b383

import requests as rqs

r = rqs.get(
	"http://127.0.0.1:8000/lampu/",
	headers = {"Authorization" : "Token f7641f4d0aecb6915a2bff70541ef4ecacc4b383"}
	)
print(r.text)