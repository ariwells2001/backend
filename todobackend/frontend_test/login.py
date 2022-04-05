import requests,json

end_point = 'http://localhost:8000/api/login/'

data = {
    'username':'iotuser',
    'password':'iot12345',
}

data = json.dumps(data)

response = requests.post(url=end_point,data=data)
data = json.loads(response.text)
status = response

print('token is {} and status is {}'.format(data,status))