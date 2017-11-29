# adaptiveprojectbackend
Adaptive Web Study Genie backend


1] System Setup 
# To be added later
export DJANGO_SETTINGS_MODULE=app_db.settings.local
export PYTHONPATH=$(pwd)



2] API sample calls with outputs

### Please note that almost all input and return parameters are strings even if values are numbers (example: card ids or noofupvotes)


2.1) POST http://ec2-18-221-144-47.us-east-2.compute.amazonaws.com/userservice/createuser/

import requests, json
headers = {'content-type':'application/json', 'Origin':['POST','PUT','DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH'] }
url = 'http://ec2-18-221-144-47.us-east-2.compute.amazonaws.com/userservice/createuser/'
```
data = {'email':'surajshah@asu.edu','pswd':'a','details':{'first_name':'Suraj','last_name':'Shah'} }
```
# Add any additional user parameters in 'details' subdict
response = requests.post(url,headers=headers,data=json.dumps(data))
print response.text
```
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
```
# Format for unsuccessful response which will be constant across all apis:
```
{
   'success': False, 
   'errorMessage': 'Internal server error',
   'errorCode': 500
}
```


2.2) POST http://ec2-18-221-144-47.us-east-2.compute.amazonaws.com/userservice/uservalidation/

import requests, json
headers = {'content-type':'application/json', 'Origin':['POST','PUT','DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH']}
url = 'http://ec2-18-221-144-47.us-east-2.compute.amazonaws.com/userservice/uservalidation/'
data = {'email':'surajshah@asu.edu','pswd':'a', 'remember_me':'1'}
#remember_me=1 will permanently set user session, any other value will not
response = requests.post(url,headers=headers,data=json.dumps(data))
print response.text
```
{
    "responseData": {
        "content": {
            "X-Authorization-Token": "e1fd5727-653f-4def-a20b-7b428cc34fed", 
            "is_authorized": true, 
            "username": "surajshah@asu.edu"
        }, 
        "status": 200, 
        "success": true
    }
}
```



2.3) POST http://ec2-18-221-144-47.us-east-2.compute.amazonaws.com/cardservice/createcard/

import requests, json
#dont forget to replace the value of X-Authorization-Token you get after login into the header below. Each token is good for 30days
headers = {'content-type':'application/json', 'Origin':['POST','PUT','DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH'], 'X-Authorization-Token': 'e1fd5727-653f-4def-a20b-7b428cc34fed'}
url = 'http://ec2-18-221-144-47.us-east-2.compute.amazonaws.com/cardservice/createcard/'
data = {'title':'Programming OOPS', 'content':'Abstraction, Polymorphism, Encapsulation, Inheritence', 'type':'0', 'tags':['oops', 'c++','java'],
'upVote':'3','downVote':'1'}
#upVote and downVote are optional
#type can be 0 or 1, try to send all tags in lowercase and trimmed
response = requests.post(url,headers=headers,data=json.dumps(data))
print response.text
```
{
    "responseData": {
        "message": "Successfully created cheatsheet", 
        "status": 200, 
        "success": true
    }
}
```


2.4) GET http://ec2-18-221-144-47.us-east-2.compute.amazonaws.com/cardservice/getallcards/

import requests, json
#dont forget to replace the value of X-Authorization-Token you get after login into the header below. Each token is good for 30days
headers = {'content-type':'application/json', 'Origin':['POST','PUT','DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH'], 'X-Authorization-Token': 'e1fd5727-653f-4def-a20b-7b428cc34fed'}
url = 'http://ec2-18-221-144-47.us-east-2.compute.amazonaws.com/cardservice/getallcards/'
#returns all cards based on most recently created/modified first - can be changed to get order according to recommendation algo
response = requests.get(url,headers=headers)
print response.text
```
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
```


2.5) POST http://ec2-18-221-144-47.us-east-2.compute.amazonaws.com/cardservice/updatecard/

import requests, json
#dont forget to replace the value of X-Authorization-Token you get after login into the header below. Each token is good for 30days
headers = {'content-type':'application/json', 'Origin':['POST','PUT','DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH'], 'X-Authorization-Token': 'e1fd5727-653f-4def-a20b-7b428cc34fed'}
url = 'http://ec2-18-221-144-47.us-east-2.compute.amazonaws.com/cardservice/updatecard/'
data = {'id':'2', 'title':'OOPS Concepts', 'content':'Abstraction, Encapsulation, Inheritence', 'type':'0', 'tags':['oops','concepts']}
#All tags before will be deleted and new sent will be added. Make sure you send the old ones if you want them to be retained
#type can be 0 or 1, try to send all tags in lowercase and trimmed
response = requests.post(url,headers=headers,data=json.dumps(data))
print response.text
```
{
    "responseData": {
        "message": "Successfully updated cheatsheet", 
        "status": 200, 
        "success": true
    }
}
```


2.6) POST http://ec2-18-221-144-47.us-east-2.compute.amazonaws.com/cardservice/deletecard/

import requests, json
#dont forget to replace the value of X-Authorization-Token you get after login into the header below. Each token is good for 30days
headers = {'content-type':'application/json', 'Origin':['POST','PUT','DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH'], 'X-Authorization-Token': 'e1fd5727-653f-4def-a20b-7b428cc34fed'}
url = 'http://ec2-18-221-144-47.us-east-2.compute.amazonaws.com/cardservice/deletecard/'
#I created the 1st card again so it got assigned id=2, which i deleted here. the id is returned in getallcards api
data = {'id':'2'}
response = requests.post(url,headers=headers,data=json.dumps(data))
print response.text
```
{
    "responseData": {
        "message": "Successfully deleted cheatsheet", 
        "status": 200, 
        "success": true
    }
}
```



2.7) POST http://ec2-18-221-144-47.us-east-2.compute.amazonaws.com/cardservice/upvote/

import requests, json
#dont forget to replace the value of X-Authorization-Token you get after login into the header below. Each token is good for 30days
headers = {'content-type':'application/json', 'Origin':['POST','PUT','DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH'], 'X-Authorization-Token': 'e1fd5727-653f-4def-a20b-7b428cc34fed'}
url = 'http://ec2-18-221-144-47.us-east-2.compute.amazonaws.com/cardservice/upvote/'
data = {'id':'1'}
response = requests.post(url,headers=headers,data=json.dumps(data))
print response.text
```
{
    "responseData": {
        "message": "Successfully upvoted cheatsheet", 
        "status": 200, 
        "success": true
    }
}
```


2.8) POST http://ec2-18-221-144-47.us-east-2.compute.amazonaws.com/cardservice/downvote/

import requests, json
#dont forget to replace the value of X-Authorization-Token you get after login into the header below. Each token is good for 30days
headers = {'content-type':'application/json', 'Origin':['POST','PUT','DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH'], 'X-Authorization-Token': 'e1fd5727-653f-4def-a20b-7b428cc34fed'}
url = 'http://ec2-18-221-144-47.us-east-2.compute.amazonaws.com/cardservice/downvote/'
data = {'id':'1'}
response = requests.post(url,headers=headers,data=json.dumps(data))
print response.text
```
{
    "responseData": {
        "message": "Successfully downvoted cheatsheet", 
        "status": 200, 
        "success": true
    }
}
```


2.9) POST http://ec2-18-221-144-47.us-east-2.compute.amazonaws.com/cardservice/favorite/

import requests, json
#dont forget to replace the value of X-Authorization-Token you get after login into the header below. Each token is good for 30days
headers = {'content-type':'application/json', 'Origin':['POST','PUT','DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH'], 'X-Authorization-Token': 'e1fd5727-653f-4def-a20b-7b428cc34fed'}
url = 'http://ec2-18-221-144-47.us-east-2.compute.amazonaws.com/cardservice/favorite/'
data = {'id':'1'}
#Automatically identifies if the user had favorited the item or not and switches between true and false so you can highlight or remove star-color
response = requests.post(url,headers=headers,data=json.dumps(data))
print response.text
```
{
    "responseData": {
        "favorite": true, 
        "id": "1", 
        "message": "Successfully saved changes", 
        "status": 200, 
        "success": true
    }
}
```


2.10) POST http://ec2-18-221-144-47.us-east-2.compute.amazonaws.com/cardservice/userlogs/

import requests, json
#dont forget to replace the value of X-Authorization-Token you get after login into the header below. Each token is good for 30days
headers = {'content-type':'application/json', 'Origin':['POST','PUT','DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH'], 'X-Authorization-Token': 'e1fd5727-653f-4def-a20b-7b428cc34fed'}
url = 'http://ec2-18-221-144-47.us-east-2.compute.amazonaws.com/cardservice/userlogs/'
data = {'id':'1', 'action':'open'}
#Call will fail if a cheatsheetid is not sent. action parameters can be lowercase - ['open','close','update','upvote','downvote','favorite','unfavorite'] or anything else you want to include and standardize. Make a call to this api on any UI action you find significant. I can give you more api parameter support too - like time spent on each cheatsheet or highlighted portion if you need it later on.
response = requests.post(url,headers=headers,data=json.dumps(data))
print response.text
```
{
    "responseData": {
        "message": "Successfully logged user activity", 
        "status": 200, 
        "success": true
    }
}
```


2.11) GET http://ec2-18-221-144-47.us-east-2.compute.amazonaws.com/cardservice/rawsearch/?search=<value>

import requests, json
headers = {'content-type':'application/json', 'Origin':['POST','PUT','DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH'], 'X-Authorization-Token': 'e1fd5727-653f-4def-a20b-7b428cc34fed'}
url = 'http://ec2-18-221-144-47.us-east-2.compute.amazonaws.com/cardservice/rawsearch/?search=Java'
response = requests.get(url,headers=headers)
print response.text
#All same format like getallcheatsheets, except the fact that there's an additional score parameter too
```
{
    "responseData": {
        "result": [
            {
                "content": "It is a \u201cscripting\u201d language, nothing to do with Java (java is all purpose lang).<br>It is interpreted language, scripts are executed without compilation.<br>Usually embedded in HTML pages &amp; add interactivity to HTML pages.<br>It will be executed immediately while the page loads into your browser. (sometimes, it is not what we want; we may want to execute when user trigger it or when the page loads)<br>JavaScript is case sensitive. (same as Java)<div><b>When to use JS?</b></div><div>Form validation.<br>React to events, even when the page is finished loading, including read and update the HTML content.<br>Offload a busy server.<br>Communicate to the browser.<br>Can create&nbsp;cookies<span style=\"background-color: transparent; font-size: 18pt; font-family: Arial; color: rgb(89, 89, 89); vertical-align: baseline; white-space: pre-wrap;\"> </span>to store and retrieve information on your computer.</div>", 
                "created_on": "2017-11-23 03:42:14.587902+00:00", 
                "downvotes": "0", 
                "favorite": false, 
                "id": "234", 
                "last_modified": "2017-11-23 03:42:14.587927+00:00", 
                "owner": "BBB User 2", 
                "score": "6.987784", 
                "tags": [
                    "communicate", 
                    "javascript", 
                    "java", 
                    "html", 
                    "HTML"
                ], 
                "title": "JS intro", 
                "type": "0", 
                "upvotes": "0"
            }, 
            {
                "content": "It is a \u201cscripting\u201d language, nothing to do with Java (java is all purpose lang).It is interpreted language, scripts are executed without compilation.Usually embedded in HTML pages & add interactivity to HTML pages.It will be executed immediately while the page loads into your browser. (sometimes, it is not what we want; we may want to execute when user trigger it or when the page loads)JavaScript is case sensitive. (same as Java)", 
                "created_on": "2017-11-23 03:42:21.927592+00:00", 
                "downvotes": "0", 
                "favorite": false, 
                "id": "449", 
                "last_modified": "2017-11-23 03:42:21.927617+00:00", 
                "owner": "CCC User 3", 
                "score": "5.572879", 
                "tags": [
                    "javascript", 
                    "java", 
                    "html", 
                    "Javascript"
                ], 
                "title": "What is JavaScript?", 
                "type": "1", 
                "upvotes": "0"
            }, 
            {
                "content": "<ul><li>Client- browser, codes are visibile, doesn't require server to create data</li><li>Server- codes are invisible in page source, provide data to on browser but does not reside on the browser</li></ul>", 
                "created_on": "2017-11-23 03:42:20.924882+00:00", 
                "downvotes": "0", 
                "favorite": false, 
                "id": "418", 
                "last_modified": "2017-11-23 03:42:20.924907+00:00", 
                "owner": "CCC User 3", 
                "score": "4.97207", 
                "tags": [
                    "Java"
                ], 
                "title": "Client/Server", 
                "type": "0", 
                "upvotes": "0"
            }
        ], 
        "status": 200, 
        "success": true
    }
}
```




2.12) GET http://ec2-18-221-144-47.us-east-2.compute.amazonaws.com/cardservice/tagsearch/?search=<value>

import requests, json
headers = {'content-type':'application/json', 'Origin':['POST','PUT','DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH'], 'X-Authorization-Token': 'e1fd5727-653f-4def-a20b-7b428cc34fed'}
url = 'http://ec2-18-221-144-47.us-east-2.compute.amazonaws.com/cardservice/tagsearch/?search=Java'
response = requests.get(url,headers=headers)
print response.text
'''
{
    "responseData": {
        "result": [
            {
                "content": "<ul><li>Client- browser, codes are visibile, doesn't require server to create data</li><li>Server- codes are invisible in page source, provide data to on browser but does not reside on the browser</li></ul>", 
                "created_on": "2017-11-23 03:42:20.924882+00:00", 
                "downvotes": "0", 
                "favorite": false, 
                "id": "418", 
                "last_modified": "2017-11-23 03:42:20.924907+00:00", 
                "owner": "CCC User 3", 
                "score": "4.97207", 
                "tags": [
                    "Java"
                ], 
                "title": "Client/Server", 
                "type": "0", 
                "upvotes": "0"
            }, 
            {
                "content": "for(int i = 0; i < n; i++) {//code goes here}", 
                "created_on": "2017-11-23 03:42:07.157217+00:00", 
                "downvotes": "0", 
                "favorite": false, 
                "id": "31", 
                "last_modified": "2017-11-23 03:42:07.157243+00:00", 
                "owner": "AAA User 1", 
                "score": "4.676841", 
                "tags": [
                    "Java"
                ], 
                "title": "For loops", 
                "type": "1", 
                "upvotes": "0"
            }, 
            {
                "content": "var employeeListObj = JSON.parse(gameText);employeeListObj.employees.length;employeeListObj.employees[0].firstName;//John*<a href=\"url\">link text</a>", 
                "created_on": "2017-11-23 03:42:24.044395+00:00", 
                "downvotes": "0", 
                "favorite": false, 
                "id": "510", 
                "last_modified": "2017-11-23 03:42:24.044418+00:00", 
                "owner": "CCC User 3", 
                "score": "4.676841", 
                "tags": [
                    "Java"
                ], 
                "title": "", 
                "type": "1", 
                "upvotes": "0"
            }
        ], 
        "status": 200, 
        "success": true
    }
}

'''







