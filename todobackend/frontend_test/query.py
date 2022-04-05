import requests,json

end_point = 'http://127.0.0.1:8000/api/todos/'

data = {
    'username':'iotuser2',
    'password':'iot12345',
    'email':'ariwells2002@gmail.com'
}

token = '7ebcdc398f5faf51984470a05a37f26ea822888b'
data = json.dumps(data)
headers = {
    'Authorization': 'Token {}'.format(token)
}
response = requests.get(url=end_point,headers=headers)
data = json.loads(response.text)
status = response

print('data is {} and status is {}'.format(data,status))