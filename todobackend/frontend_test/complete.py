import requests,json

end_point = 'http://127.0.0.1:8000/api/todos/4/complete'

# data = {
#     'username':'iotuser1',
#     'password':'iot12345',
# }

# data = json.dumps(data)

headers = {
    'Authorization': 'Token 488620c0fb0f7b1cb48cb14e525107d45c4d75c5'
}

response = requests.put(url=end_point,headers=headers)
data = json.loads(response.text)
status = response

print('data is {} and status is {}'.format(data,status))