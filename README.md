# adaptiveprojectbackend
Adaptive Web Study Genie backend


1] System Setup 
#To be added later
export DJANGO_SETTINGS_MODULE=app_db.settings.local
export PYTHONPATH=$(pwd)



2] API sample calls with outputs

###Please note that almost all input and return parameters are strings even if values are numbers (example: card ids or noofupvotes)
#Replace localhost:7285 with domain ec2-18-221-144-47.us-east-2.compute.amazonaws.com


2.1) POST http://localhost:7285/userservice/createuser/

import requests, json
headers = {'content-type':'application/json', 'Origin':['POST','PUT','DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH'] }
url = 'http://127.0.0.1:7285/userservice/createuser/'
data = {'email':'surajshah@asu.edu','pswd':'a','details':{'first_name':'Suraj','last_name':'Shah'} }
#Add any additional user parameters in 'details' subdict
response = requests.post(url,headers=headers,data=json.dumps(data))
print response.text
"""
{
	"responseData": {
		"content": {
			"X-Authorization-Token": "845e3b0d-090c-44a2-9589-6e32d71e4466", 
			"username": "surajshah@asu.edu"
		}, 
		"status": 201, 
		"success": true
	}
}
"""
#Format for unsuccessful response which will be constant across all apis:
"""
{
   'success': False, 
   'errorMessage': 'Internal server error',
   'errorCode': 500
}
"""


2.2) POST http://127.0.0.1:7285/userservice/uservalidation/

import requests, json
headers = {'content-type':'application/json', 'Origin':['POST','PUT','DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH']}
url = 'http://127.0.0.1:7285/userservice/uservalidation/'
data = {'email':'surajshah@asu.edu','pswd':'a', 'remember_me':'1'}
#remember_me=1 will permanently set user session, any other value will not
response = requests.post(url,headers=headers,data=json.dumps(data))
print response.text
"""
{
    "responseData": {
        "content": {
            "X-Authorization-Token": "93d3505b-71ca-4912-9981-efd94e5c40bc", 
            "is_authorized": true, 
            "username": "surajshah@asu.edu"
        }, 
        "status": 200, 
        "success": true
    }
}
"""



2.3) POST http://127.0.0.1:7285/cardservice/createcard/

import requests, json
#dont forget to replace the value of X-Authorization-Token you get after login into the header below. Each token is good for 30days
headers = {'content-type':'application/json', 'Origin':['POST','PUT','DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH'], 'X-Authorization-Token': '93d3505b-71ca-4912-9981-efd94e5c40bc'}
url = 'http://127.0.0.1:7285/cardservice/createcard/'
data = {'title':'Programming OOPS', 'content':'Abstraction, Polymorphism, Encapsulation, Inheritence', 'type':'0', 'tags':['oops', 'c++','java']}
#type can be 0 or 1, try to send all tags in lowercase and trimmed
response = requests.post(url,headers=headers,data=json.dumps(data))
print response.text
"""
{
    "responseData": {
        "message": "Successfully created cheatsheet", 
        "status": 200, 
        "success": true
    }
}
"""


2.4) GET http://127.0.0.1:7285/cardservice/getallcards/

import requests, json
#dont forget to replace the value of X-Authorization-Token you get after login into the header below. Each token is good for 30days
headers = {'content-type':'application/json', 'Origin':['POST','PUT','DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH'], 'X-Authorization-Token': '93d3505b-71ca-4912-9981-efd94e5c40bc'}
url = 'http://127.0.0.1:7285/cardservice/getallcards/'
#returns all cards based on most recently created/modified first - can be changed to get order according to recommendation algo
response = requests.get(url,headers=headers)
print response.text
"""
{
    "responseData": {
        "result": [
            {
                "content": "Abstraction, Polymorphism, Encapsulation, Inheritence", 
                "created_on": "2017-11-16 06:33:49.870317+00:00", 
                "downvotes": "0", 
                "favorite": false, 
                "id": "1", 
                "last_modified": "2017-11-16 06:33:49.870352+00:00", 
                "owner": "Suraj Shah", 
                "tags": [
                    "java", 
                    "c++", 
                    "oops"
                ], 
                "title": "Programming OOPS", 
                "type": "0", 
                "upvotes": "0"
            }
        ], 
        "status": 200, 
        "success": true
    }
}
"""


2.5) POST http://127.0.0.1:7285/cardservice/updatecard/

import requests, json
#dont forget to replace the value of X-Authorization-Token you get after login into the header below. Each token is good for 30days
headers = {'content-type':'application/json', 'Origin':['POST','PUT','DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH'], 'X-Authorization-Token': '93d3505b-71ca-4912-9981-efd94e5c40bc'}
url = 'http://127.0.0.1:7285/cardservice/updatecard/'
data = {'id':'1', 'title':'OOPS Concepts', 'content':'Abstraction, Encapsulation, Inheritence', 'type':'0', 'tags':['oops','concepts']}
#All tags before will be deleted and new sent will be added. Make sure you send the old ones if you want them to be retained
#type can be 0 or 1, try to send all tags in lowercase and trimmed
response = requests.post(url,headers=headers,data=json.dumps(data))
print response.text
"""
{
    "responseData": {
        "message": "Successfully updated cheatsheet", 
        "status": 200, 
        "success": true
    }
}
"""


2.6) POST http://127.0.0.1:7285/cardservice/deletecard/

import requests, json
#dont forget to replace the value of X-Authorization-Token you get after login into the header below. Each token is good for 30days
headers = {'content-type':'application/json', 'Origin':['POST','PUT','DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH'], 'X-Authorization-Token': '93d3505b-71ca-4912-9981-efd94e5c40bc'}
url = 'http://127.0.0.1:7285/cardservice/deletecard/'
#I created the 1st card again so it got assigned id=2, which i deleted here. the id is returned in getallcards api
data = {'id':'2'}
response = requests.post(url,headers=headers,data=json.dumps(data))
print response.text
"""
{
    "responseData": {
        "message": "Successfully deleted cheatsheet", 
        "status": 200, 
        "success": true
    }
}
"""



2.7) POST http://127.0.0.1:7285/cardservice/upvote/

import requests, json
#dont forget to replace the value of X-Authorization-Token you get after login into the header below. Each token is good for 30days
headers = {'content-type':'application/json', 'Origin':['POST','PUT','DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH'], 'X-Authorization-Token': '93d3505b-71ca-4912-9981-efd94e5c40bc'}
url = 'http://127.0.0.1:7285/cardservice/upvote/'
data = {'id':'1'}
response = requests.post(url,headers=headers,data=json.dumps(data))
print response.text
"""
{
    "responseData": {
        "message": "Successfully upvoted cheatsheet", 
        "status": 200, 
        "success": true
    }
}
"""


2.8) POST http://127.0.0.1:7285/cardservice/downvote/

import requests, json
#dont forget to replace the value of X-Authorization-Token you get after login into the header below. Each token is good for 30days
headers = {'content-type':'application/json', 'Origin':['POST','PUT','DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH'], 'X-Authorization-Token': '93d3505b-71ca-4912-9981-efd94e5c40bc'}
url = 'http://127.0.0.1:7285/cardservice/downvote/'
data = {'id':'1'}
response = requests.post(url,headers=headers,data=json.dumps(data))
print response.text
"""
{
    "responseData": {
        "message": "Successfully downvoted cheatsheet", 
        "status": 200, 
        "success": true
    }
}
"""


2.9) POST http://127.0.0.1:7285/cardservice/favorite/

import requests, json
#dont forget to replace the value of X-Authorization-Token you get after login into the header below. Each token is good for 30days
headers = {'content-type':'application/json', 'Origin':['POST','PUT','DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH'], 'X-Authorization-Token': '93d3505b-71ca-4912-9981-efd94e5c40bc'}
url = 'http://127.0.0.1:7285/cardservice/favorite/'
data = {'id':'1'}
#Automatically identifies if the user had favorited the item or not and switches between true and false so you can highlight or remove star-color
response = requests.post(url,headers=headers,data=json.dumps(data))
print response.text
"""
{
    "responseData": {
        "favorite": true, 
        "id": "1", 
        "message": "Successfully saved changes", 
        "status": 200, 
        "success": true
    }
}
"""


2.10) POST http://127.0.0.1:7285/cardservice/userlogs/

import requests, json
#dont forget to replace the value of X-Authorization-Token you get after login into the header below. Each token is good for 30days
headers = {'content-type':'application/json', 'Origin':['POST','PUT','DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH'], 'X-Authorization-Token': '93d3505b-71ca-4912-9981-efd94e5c40bc'}
url = 'http://127.0.0.1:7285/cardservice/userlogs/'
data = {'id':'1', 'action':'open'}
#Call will fail if a cheatsheetid is not sent. action parameters can be lowercase - ['open','close','update','upvote','downvote','favorite','unfavorite'] or anything else you want to include and standardize. Make a call to this api on any UI action you find significant. I can give you more api parameter support too - like time spent on each cheatsheet or highlighted portion if you need it later on.
response = requests.post(url,headers=headers,data=json.dumps(data))
print response.text
"""
{
    "responseData": {
        "message": "Successfully logged user activity", 
        "status": 200, 
        "success": true
    }
}
"""
