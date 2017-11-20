import requests, json

headers = {'content-type':'application/json'}
url = 'http://ec2-18-221-144-47.us-east-2.compute.amazonaws.com/userservice/createuser/'
# data = {'email':'aaa@gmail.com','pswd':'123','details':{'first_name':'AAA','last_name':'User 1'}} # "X-Authorization-Token": "089b2d64-1c0f-4457-85dc-7060e3f5fdc7"
# data = {'email':'bbb@gmail.com','pswd':'123','details':{'first_name':'BBB','last_name':'User 2'}} #  "X-Authorization-Token": "e46cc17e-cc4b-49e6-a7f5-bd9fe387beea"
# data = {'email':'ccc@gmail.com','pswd':'123','details':{'first_name':'CCC','last_name':'User 3'}} # "X-Authorization-Token": "c8bdd3b0-2277-4462-ba1d-f7a3d02da9e9"
response = requests.post(url,headers=headers,data=json.dumps(data))
print response.text
