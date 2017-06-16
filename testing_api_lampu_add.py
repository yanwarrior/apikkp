# Token f7641f4d0aecb6915a2bff70541ef4ecacc4b383

import requests as rqs
import json

r = rqs.post(
	"http://127.0.0.1:8000/lampu/add/",
	headers = {"Authorization" : "Token f7641f4d0aecb6915a2bff70541ef4ecacc4b383"},
	data = json.dumps({'nama':'Lampu Merah','status':True})
	)