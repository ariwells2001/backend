import requests,json

end_point = 'http://127.0.0.1:8000/api/signup/'

data = {
    'username':'iotuser3133333',
    'password':'iot123451',
    'email':'ariwellxxxxx@hotmail1.com'
}

data = json.dumps(data)

response = requests.post(url=end_point,data=data)
data = json.loads(response.text)
status = response

print('token is {} and status is {}'.format(data,status))