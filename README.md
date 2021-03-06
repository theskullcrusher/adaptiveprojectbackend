# adaptiveprojectbackend
Adaptive Web Study Genie backend


1] System Setup 
#Run install_packages.sh shell script in home folder
#go to app_db and run pip install -r requirements.txt
#then export this
export DJANGO_SETTINGS_MODULE=app_db.settings.local
#now run python setup.py develop to install library
#now run python manage.py migrate       #to setup the database
#make sure ur mysql user is root, password is surajshah and dbname is app
#go to app_service
#export
export PYTHONPATH=$(pwd)



2] API sample calls with outputs

### Please note that almost all input and return parameters are strings even if values are numbers (example: card ids or noofupvotes)


2.1) POST http://ec2-34-214-219-216.us-west-2.compute.amazonaws.com/userservice/createuser/

import requests, json
headers = {'content-type':'application/json', 'Origin':['POST','PUT','DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH'] }
url = 'http://ec2-34-214-219-216.us-west-2.compute.amazonaws.com/userservice/createuser/'
```
data = {'email':'suraj@asu.edu','pswd':'a','details':{'first_name':'Suraj','last_name':'Shah'} }
```
# Add any additional user parameters in 'details' subdict
response = requests.post(url,headers=headers,data=json.dumps(data))
print response.text
```
{
	"responseData": {
		"content": {
			"X-Authorization-Token": "da26892b-bf84-4a7b-9e46-37560c5b9661", 
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


2.2) POST http://ec2-34-214-219-216.us-west-2.compute.amazonaws.com/userservice/uservalidation/

import requests, json
headers = {'content-type':'application/json', 'Origin':['POST','PUT','DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH']}
url = 'http://ec2-34-214-219-216.us-west-2.compute.amazonaws.com/userservice/uservalidation/'
data = {'email':'ssshah22@asu.edu','pswd':'a', 'remember_me':'1'}
#remember_me=1 will permanently set user session, any other value will not
response = requests.post(url,headers=headers,data=json.dumps(data))
print response.text
```
{
    "responseData": {
        "content": {
            "X-Authorization-Token": "da26892b-bf84-4a7b-9e46-37560c5b9661", 
            "is_authorized": true, 
            "username": "surajshah@asu.edu"
        }, 
        "status": 200, 
        "success": true
    }
}
```



2.3) POST http://ec2-34-214-219-216.us-west-2.compute.amazonaws.com/cardservice/createcard/

import requests, json
#dont forget to replace the value of X-Authorization-Token you get after login into the header below. Each token is good for 30days
headers = {'content-type':'application/json', 'Origin':['POST','PUT','DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH'], 'X-Authorization-Token': 'da26892b-bf84-4a7b-9e46-37560c5b9661'}
url = 'http://ec2-34-214-219-216.us-west-2.compute.amazonaws.com/cardservice/createcard/'
data = {'title':'Tempe Test lorem epsum', 'content':'Abstraction, Polymorphism, Encapsulation, Inheritence', 'type':'0', 'tags':['oops', 'c++','java'],
'upVote':'3','downVote':'1', 'private':True, 'in_group':False}
##If in_group is true - send another parameter 'group':'<id>' which tells which group to add the card to
#private defines access level of card
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

###Createcard for a group

POST http://ec2-34-214-219-216.us-west-2.compute.amazonaws.com/cardservice/createcard/

import requests, json
#dont forget to replace the value of X-Authorization-Token you get after login into the header below. Each token is good for 30days
headers = {'content-type':'application/json', 'Origin':['POST','PUT','DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH'], 'X-Authorization-Token': 'da26892b-bf84-4a7b-9e46-37560c5b9661'}
url = 'http://ec2-34-214-219-216.us-west-2.compute.amazonaws.com/cardservice/createcard/'
data = {'title':'Tempe Test lorem epsum', 'content':'Abstraction, Polymorphism, Encapsulation, Inheritence', 'type':'0', 'tags':['oops', 'c++','java'],
'upVote':'3','downVote':'1', 'private':True, 'in_group':True, 'group':'3'}
##If in_group is true - send another parameter 'group':'<id>' which tells which group to add the card to
response = requests.post(url,headers=headers,data=json.dumps(data))
print response.text







2.4) GET http://ec2-34-214-219-216.us-west-2.compute.amazonaws.com/cardservice/getallcards/

import requests, json
#dont forget to replace the value of X-Authorization-Token you get after login into the header below. Each token is good for 30days
headers = {'content-type':'application/json', 'Origin':['POST','PUT','DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH'], 'X-Authorization-Token': 'da26892b-bf84-4a7b-9e46-37560c5b9661'}
url = 'http://ec2-34-214-219-216.us-west-2.compute.amazonaws.com/cardservice/getallcards/'
#returns all cards based on most recently created/modified first - can be changed to get order according to recommendation algo
response = requests.get(url,headers=headers)
print response.text
```
{
    "responseData": {
        "result": [
            {
                "content": "test content yada yad", 
                "created_on": "2017-11-21 22:37:41.044169+00:00", 
                "downvotes": "0", 
                "favorite": false, 
                "id": "2", 
                "last_modified": "2017-11-23 02:25:24.844200+00:00", 
                "owner": "aaa aaa", 
                "owner_id": "12", 
                "tags": [
                    "tag 1", 
                    "tag 2", 
                    "tag 3"
                ], 
                "title": "lorem ipsum", 
                "type": "0", 
                "upvotes": "0", 
                "user_owner": false,
                "private": false
            }, 
            {
                "content": "Abstract, Inherit", 
                "created_on": "2017-11-22 23:55:08.382566+00:00", 
                "downvotes": "0", 
                "favorite": false, 
                "id": "3", 
                "last_modified": "2017-11-22 23:57:20.875366+00:00", 
                "owner": "Suraj Shah", 
                "owner_id": "1", 
                "tags": [
                    "oops"
                ], 
                "title": "OOPSIEEE Concepts", 
                "type": "0", 
                "upvotes": "0", 
                "user_owner": true,
                "private": false
            }
        ], 
        "status": 200, 
        "success": true
    }
}
```


2.5) POST http://ec2-34-214-219-216.us-west-2.compute.amazonaws.com/cardservice/updatecard/

import requests, json
#dont forget to replace the value of X-Authorization-Token you get after login into the header below. Each token is good for 30days
headers = {'content-type':'application/json', 'Origin':['POST','PUT','DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH'], 'X-Authorization-Token': 'da26892b-bf84-4a7b-9e46-37560c5b9661'}
url = 'http://ec2-34-214-219-216.us-west-2.compute.amazonaws.com/cardservice/updatecard/'
data = {'id':'100', 'title':'OOPS Concepts', 'content':'Abstraction, Encapsulation, Inheritence', 'type':'0', 'tags':['oops','concepts'], 'private':True}
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


2.6) POST http://ec2-34-214-219-216.us-west-2.compute.amazonaws.com/cardservice/deletecard/

import requests, json
#dont forget to replace the value of X-Authorization-Token you get after login into the header below. Each token is good for 30days
headers = {'content-type':'application/json', 'Origin':['POST','PUT','DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH'], 'X-Authorization-Token': 'da26892b-bf84-4a7b-9e46-37560c5b9661'}
url = 'http://ec2-34-214-219-216.us-west-2.compute.amazonaws.com/cardservice/deletecard/'
#I created the 1st card again so it got assigned id=2, which i deleted here. the id is returned in getallcards api
data = {'id':'3'}
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



2.7) POST http://ec2-34-214-219-216.us-west-2.compute.amazonaws.com/cardservice/upvote/

import requests, json
#dont forget to replace the value of X-Authorization-Token you get after login into the header below. Each token is good for 30days
headers = {'content-type':'application/json', 'Origin':['POST','PUT','DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH'], 'X-Authorization-Token': 'da26892b-bf84-4a7b-9e46-37560c5b9661'}
url = 'http://ec2-34-214-219-216.us-west-2.compute.amazonaws.com/cardservice/upvote/'
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


2.8) POST http://ec2-34-214-219-216.us-west-2.compute.amazonaws.com/cardservice/downvote/

import requests, json
#dont forget to replace the value of X-Authorization-Token you get after login into the header below. Each token is good for 30days
headers = {'content-type':'application/json', 'Origin':['POST','PUT','DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH'], 'X-Authorization-Token': 'da26892b-bf84-4a7b-9e46-37560c5b9661'}
url = 'http://ec2-34-214-219-216.us-west-2.compute.amazonaws.com/cardservice/downvote/'
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


2.9) POST http://ec2-34-214-219-216.us-west-2.compute.amazonaws.com/cardservice/favorite/

import requests, json
#dont forget to replace the value of X-Authorization-Token you get after login into the header below. Each token is good for 30days
headers = {'content-type':'application/json', 'Origin':['POST','PUT','DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH'], 'X-Authorization-Token': 'da26892b-bf84-4a7b-9e46-37560c5b9661'}
url = 'http://ec2-34-214-219-216.us-west-2.compute.amazonaws.com/cardservice/favorite/'
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


2.10) POST http://ec2-34-214-219-216.us-west-2.compute.amazonaws.com/cardservice/userlogs/

import requests, json
#dont forget to replace the value of X-Authorization-Token you get after login into the header below. Each token is good for 30days
headers = {'content-type':'application/json', 'Origin':['POST','PUT','DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH'], 'X-Authorization-Token': 'da26892b-bf84-4a7b-9e46-37560c5b9661'}
url = 'http://ec2-34-214-219-216.us-west-2.compute.amazonaws.com/cardservice/userlogs/'
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


2.11) GET http://ec2-34-214-219-216.us-west-2.compute.amazonaws.com/cardservice/rawsearch/?search=<value>

import requests, json
headers = {'content-type':'application/json', 'Origin':['POST','PUT','DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH'], 'X-Authorization-Token': 'da26892b-bf84-4a7b-9e46-37560c5b9661'}
url = 'http://ec2-34-214-219-216.us-west-2.compute.amazonaws.com/cardservice/rawsearch/?search=Java'
response = requests.get(url,headers=headers)
print response.text
#All same format like getallcheatsheets, except the fact that there's an additional score parameter too
```
{
    "responseData": {
        "result": [
            {
                "content": "for(i=0; i<cars.length;i++){  text+=cars[i]+\"<br>\"  }    Loops that are used to go through a code more than once for different outputs.", 
                "created_on": "2017-11-23 03:42:12.848887+00:00", 
                "downvotes": "0", 
                "favorite": false, 
                "id": "176", 
                "last_modified": "2017-11-23 03:42:12.848912+00:00", 
                "owner": "AAA User 1", 
                "owner_id": "14", 
                "score": "4.1118436", 
                "tags": [
                    "loops", 
                    "Javascript"
                ], 
                "title": "Java Iteration", 
                "type": "1", 
                "upvotes": "0", 
                "user_owner": false
            }, 
            {
                "content": "Two kinds<div><ul><li>Checked(Must be caught with a Try &amp; Catch or throw cause)</li><li>Unchcked(should not be caught. No throw cause</li></ul></div>", 
                "created_on": "2017-11-23 03:42:23.657257+00:00", 
                "downvotes": "0", 
                "favorite": false, 
                "id": "499", 
                "last_modified": "2017-11-23 03:42:23.657290+00:00", 
                "owner": "CCC User 3", 
                "owner_id": "16", 
                "score": "3.6080272", 
                "tags": [
                    "checked", 
                    "Java"
                ], 
                "title": "Exceptions&nbsp;", 
                "type": "0", 
                "upvotes": "0", 
                "user_owner": false,
                "in_group": false
            }
        ], 
        "status": 200, 
        "success": true
    }
}
```




2.12) GET http://ec2-34-214-219-216.us-west-2.compute.amazonaws.com/cardservice/tagsearch/?search=<value>

import requests, json
headers = {'content-type':'application/json', 'Origin':['POST','PUT','DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH'], 'X-Authorization-Token': 'da26892b-bf84-4a7b-9e46-37560c5b9661'}
url = 'http://ec2-34-214-219-216.us-west-2.compute.amazonaws.com/cardservice/tagsearch/?search=Java'
response = requests.get(url,headers=headers)
print response.text
'''
{
    "responseData": {
        "result": [
            {
                "content": "Link Example:&nbsp;&lt;a href=\"url\"&gt;link text&lt;/a&gt;<div>CSS: &lt;link rel=\"stylesheet\" href=\"style.css\"&gt;</div><div>or</div><div>&lt;style&gt;</div><div>body {background-color: maroon;}</div><div>h1 {color: blue;}</div><div>&nbsp;&lt;/style&gt;</div><div>Image: &lt;img src=\"url\" alt=\"some_text\" style=\"width:width;height:height;\"&gt;</div><div>Paragraph: &lt;p&gt;This is a paragraph.&lt;/p&gt;</div><div>HTML: &lt;html&gt; &lt;head&gt; ... &lt;/head&gt; &lt;body&gt; ... &lt;/body&gt; &lt;/html&gt;</div><div>Java: &lt;script language=\"JavaScript\"&gt; var text = document.getElementById(\"firstP\").innerHTML; window.alert(text);\t&lt;/script&gt;</div>", 
                "created_on": "2017-11-23 03:42:18.116040+00:00", 
                "downvotes": "0", 
                "favorite": false, 
                "id": "340", 
                "last_modified": "2017-11-23 03:42:18.116065+00:00", 
                "owner": "BBB User 2", 
                "owner_id": "15", 
                "score": "2.30687", 
                "tags": [
                    "javascript", 
                    "java", 
                    "image", 
                    "css", 
                    "html", 
                    "paragraph", 
                    "HTML"
                ], 
                "title": "tags", 
                "type": "0", 
                "upvotes": "0", 
                "user_owner": false,
                "in_group": false
            }, 
            {
                "content": "<p class=\"MsoNormal\" style=\"margin: 0in 0in 0.0001pt; font-size: 12pt; font-family: Calibri;\">HTML- Hyper Text Markup language, the mark up formatting language for the web<o:p></o:p></p><p class=\"MsoNormal\" style=\"margin: 0in 0in 0.0001pt; font-size: 12pt; font-family: Calibri;\"></p><p class=\"MsoNormal\" style=\"margin: 0in 0in 0.0001pt; font-size: 12pt; font-family: Calibri;\">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Language to build web pages (document structure, content presentation). html</p><p class=\"MsoNormal\" style=\"margin: 0in 0in 0.0001pt; font-size: 12pt; font-family: Calibri;\">HTML5 -&nbsp;<span style=\"width: auto; height: auto; font-family: Calibri, sans-serif; font-size: 11pt;\">similar but the latest version of hypertext Makeup language</span></p><p class=\"MsoNormal\" style=\"margin: 0in 0in 0.0001pt; font-size: 12pt; font-family: Calibri;\">XML ? extensible markup language, looks like HTML with no predefined tags, to store and to transfer data, XML tags are case sensitive and element must be properly nested<o:p></o:p></p><p class=\"MsoNormal\" style=\"margin: 0in 0in 0.0001pt; font-size: 12pt; font-family: Calibri;\">JSON(JavaScript Object Notation) ? alternate to XML, a subset of JavaScript programming language lightweight computer data interchangeable format and is language independent data format&nbsp;<o:p></o:p></p><p class=\"MsoNormal\" style=\"margin: 0in 0in 0.0001pt; font-size: 12pt; font-family: Calibri;\">Why do we need it? &nbsp;Information exchange: separate content from appearance, to store and transfer data, distributing data over the internet<o:p></o:p></p><p class=\"MsoNormal\" style=\"margin: 0in 0in 0.0001pt; font-size: 12pt; font-family: Calibri;\">JavaScript: scripting language, nothing to do with Java, to interpreted language, scripts are executed without compilation, usually embedded in HTML and add interactivity to HTML pages<o:p></o:p></p><p class=\"MsoNormal\" style=\"margin: 0in 0in 0.0001pt; font-size: 12pt; font-family: Calibri;\">Roles: HTML is to define the content of web pages<o:p></o:p></p><p class=\"MsoNormal\" style=\"margin: 0in 0in 0.0001pt; font-size: 12pt; font-family: Calibri;\">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; CSS to specify the layout of the web pages<o:p></o:p></p><p class=\"MsoNormal\" style=\"margin: 0in 0in 0.0001pt; font-size: 12pt; font-family: Calibri;\">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; JavaScript to program the behavior of the web pages<o:p></o:p></p><p class=\"MsoNormal\" style=\"margin: 0in 0in 0.0001pt; font-size: 12pt; font-family: Calibri;\">supposed to be easier that everybody can write it</p><div>URI/URL: Uniform resource Identifier</div><div>An \"address\" that is unique &amp; used to identify each</div><div>&nbsp;resource on the web.&nbsp;</div><div>HTTP: Hypertext transfer protocols&nbsp;</div><div>Allows for the retrieval of linked resources from the web. &nbsp;</div><div>CSS: Cascading Style Sheets</div><div>Used to specify the layout of a web page.&nbsp;</div>", 
                "created_on": "2017-11-23 03:42:16.796084+00:00", 
                "downvotes": "0", 
                "favorite": false, 
                "id": "304", 
                "last_modified": "2017-11-23 03:42:16.796108+00:00", 
                "owner": "BBB User 2", 
                "owner_id": "15", 
                "score": "1.8933065", 
                "tags": [
                    "html5", 
                    "javascript", 
                    "java", 
                    "roles", 
                    "css", 
                    "http", 
                    "json", 
                    "html", 
                    "xml", 
                    "identifier", 
                    "uniform", 
                    "HTML"
                ], 
                "title": "", 
                "type": "0", 
                "upvotes": "0", 
                "user_owner": false
            }
        ], 
        "status": 200, 
        "success": true
    }
}

'''


2.13) GET http://ec2-34-214-219-216.us-west-2.compute.amazonaws.com/cardservice/feed/

import requests, json
#dont forget to replace the value of X-Authorization-Token you get after login into the header below. Each token is good for 30days
headers = {'content-type':'application/json', 'Origin':['POST','PUT','DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH'], 'X-Authorization-Token': 'da26892b-bf84-4a7b-9e46-37560c5b9661'}
url = 'http://ec2-34-214-219-216.us-west-2.compute.amazonaws.com/cardservice/feed/'
#returns 10 recent feeds across the platform - all card data plus extra parameters timestamp, activity. User owner field to find the name of person who did the activity
response = requests.get(url,headers=headers)
print response.text
```
{
    "responseData": {
        "result": [
            {
                "action": "upvote", 
                "content": "testing update on card 2", 
                "created_on": "2017-11-23 02:42:52.738972+00:00", 
                "downvotes": "0", 
                "favorite": false, 
                "id": "4", 
                "last_modified": "2017-11-23 03:38:26.440532+00:00", 
                "owner": "aaa aaa", 
                "owner_id": "12", 
                "private": false, 
                "tags": [
                    "tag 1", 
                    "tag 2", 
                    "tag 3"
                ], 
                "timestamp": "2017-11-30 04:23:02.501050+00:00", 
                "title": "test update", 
                "type": "0", 
                "upvotes": "3", 
                "user_owner": false,
                "in_group": false
            }, 
            {
                "action": "favorite", 
                "content": "<ul><li>integer</li><li>float&nbsp;</li><li>String</li><li>character&nbsp;</li><li>boolean</li></ul>", 
                "created_on": "2017-11-23 03:42:06.306896+00:00", 
                "downvotes": "0", 
                "favorite": false, 
                "id": "10", 
                "last_modified": "2017-11-23 03:42:06.306921+00:00", 
                "owner": "AAA User 1", 
                "owner_id": "14", 
                "private": false, 
                "tags": [
                    "string", 
                    "HTML"
                ], 
                "timestamp": "2017-11-30 04:21:23.030236+00:00", 
                "title": "Data Types", 
                "type": "0", 
                "upvotes": "0", 
                "user_owner": false
            }
        ], 
        "status": 200, 
        "success": true
    }
}
```

2.14 POST http://ec2-34-214-219-216.us-west-2.compute.amazonaws.com/cardservice/creategroup/

import requests, json
#dont forget to replace the value of X-Authorization-Token you get after login into the header below. Each token is good for 30days
headers = {'content-type':'application/json', 'Origin':['POST','PUT','DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH'], 'X-Authorization-Token': 'da26892b-bf84-4a7b-9e46-37560c5b9661'}
url = 'http://ec2-34-214-219-216.us-west-2.compute.amazonaws.com/cardservice/creategroup/'
data = {'title':'Java Learners Group'}
response = requests.post(url,headers=headers,data=json.dumps(data))
print response.text
"""
{
    "responseData": {
        "message": "Successfully created group", 
        "status": 200, 
        "success": true
    }
}
"""

2.15 GET http://ec2-34-214-219-216.us-west-2.compute.amazonaws.com/cardservice/getgroups/

import requests, json
#dont forget to replace the value of X-Authorization-Token you get after login into the header below. Each token is good for 30days
headers = {'content-type':'application/json', 'Origin':['POST','PUT','DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH'], 'X-Authorization-Token': 'da26892b-bf84-4a7b-9e46-37560c5b9661'}
url = 'http://ec2-34-214-219-216.us-west-2.compute.amazonaws.com/cardservice/getgroups/'
response = requests.get(url,headers=headers)
print response.text
"""
{
    "responseData": {
        "result": [
            {
                "created_on": "2017-12-01 07:02:21.864486+00:00", 
                "id": "1", 
                "last_modified": "2017-12-01 07:02:21.864513+00:00", 
                "owner": "Suraj Shah", 
                "owner_id": "1", 
                "title": "Html Learners Group", 
                "user_owner": true
            }, 
            {
                "created_on": "2017-12-01 07:04:27.310516+00:00", 
                "id": "2", 
                "last_modified": "2017-12-01 07:04:27.310541+00:00", 
                "owner": "Suraj Shah", 
                "owner_id": "1", 
                "title": "Java Learners Group", 
                "user_owner": true
            }
        ], 
        "status": 200, 
        "success": true
    }
}
"""

2.16 POST http://ec2-34-214-219-216.us-west-2.compute.amazonaws.com/cardservice/deletegroup/

import requests, json
#dont forget to replace the value of X-Authorization-Token you get after login into the header below. Each token is good for 30days
headers = {'content-type':'application/json', 'Origin':['POST','PUT','DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH'], 'X-Authorization-Token': 'da26892b-bf84-4a7b-9e46-37560c5b9661'}
url = 'http://ec2-34-214-219-216.us-west-2.compute.amazonaws.com/cardservice/deletegroup/'
data = {'group':'1'}
response = requests.post(url,headers=headers,data=json.dumps(data))
print response.text
"""
{
    "responseData": {
        "message": "Successfully deleted group 1", 
        "status": 200, 
        "success": true
    }
}
"""


2.17 GET http://ec2-34-214-219-216.us-west-2.compute.amazonaws.com/cardservice/getgroupcards/?group=2

import requests, json
#dont forget to replace the value of X-Authorization-Token you get after login into the header below. Each token is good for 30days
headers = {'content-type':'application/json', 'Origin':['POST','PUT','DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH'], 'X-Authorization-Token': 'da26892b-bf84-4a7b-9e46-37560c5b9661'}
url = 'http://ec2-34-214-219-216.us-west-2.compute.amazonaws.com/cardservice/getgroupcards/?group=2'
response = requests.get(url,headers=headers)
print response.text
"""
{
    "responseData": {
        "result": [
            {
                "content": "Abstraction, Polymorphism, Encapsulation, Inheritence", 
                "created_on": "2017-12-01 07:31:40.180208+00:00", 
                "downvotes": "1", 
                "favorite": false, 
                "id": "534", 
                "in_group": true, 
                "last_modified": "2017-12-01 07:31:40.180232+00:00", 
                "owner": "Suraj Shah", 
                "owner_id": "1", 
                "private": true, 
                "tags": [
                    "java", 
                    "c++", 
                    "oops"
                ], 
                "title": "Tempe Test lorem epsum", 
                "type": "0", 
                "upvotes": "3", 
                "user_owner": true
            }
        ], 
        "status": 200, 
        "success": true
    }
}
"""


2.18 GET http://ec2-34-214-219-216.us-west-2.compute.amazonaws.com/cardservice/getusers/
or
GET http://ec2-34-214-219-216.us-west-2.compute.amazonaws.com/cardservice/getusers/?group=3

import requests, json
#dont forget to replace the value of X-Authorization-Token you get after login into the header below. Each token is good for 30days
headers = {'content-type':'application/json', 'Origin':['POST','PUT','DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH'], 'X-Authorization-Token': 'da26892b-bf84-4a7b-9e46-37560c5b9661'}
#url = 'http://ec2-34-214-219-216.us-west-2.compute.amazonaws.com/cardservice/getusers/'
url = 'http://ec2-34-214-219-216.us-west-2.compute.amazonaws.com/cardservice/getusers/?group=3'
#If group para is sent, returns all users in that group. if not sent, returns details of all users

response = requests.get(url,headers=headers)
print response.text
"""
{
    "responseData": {
        "result": [
            {
                "email": "", 
                "id": "1", 
                "name": "Suraj Shah"
            }
        ], 
        "status": 200, 
        "success": true
    }
}
"""




2.19 POST http://ec2-34-214-219-216.us-west-2.compute.amazonaws.com/cardservice/addusers/

import requests, json
#dont forget to replace the value of X-Authorization-Token you get after login into the header below. Each token is good for 30days
headers = {'content-type':'application/json', 'Origin':['POST','PUT','DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH'], 'X-Authorization-Token': 'da26892b-bf84-4a7b-9e46-37560c5b9661'}
url = 'http://ec2-34-214-219-216.us-west-2.compute.amazonaws.com/cardservice/addusers/'
data = {'group':'3', 'users':['4','5','8','16','18']}
response = requests.post(url,headers=headers,data=json.dumps(data))
print response.text
"""
{
    "responseData": {
        "message": "Successfully added users to groups", 
        "status": 200, 
        "success": true
    }
}
"""


2.20 GET http://ec2-34-214-219-216.us-west-2.compute.amazonaws.com/cardservice/recommended/

import requests, json
#dont forget to replace the value of X-Authorization-Token you get after login into the header below. Each token is good for 30days
headers = {'content-type':'application/json', 'Origin':['POST','PUT','DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH'], 'X-Authorization-Token': 'da26892b-bf84-4a7b-9e46-37560c5b9661'}
url = 'http://ec2-34-214-219-216.us-west-2.compute.amazonaws.com/cardservice/recommended/'
response = requests.get(url,headers=headers)
print response.text

##THIS WILL RETURN TOP 10 RECOMMENDED CARDS
"""
{
    "responseData": {
        "result": [
            {
                "content": "Abstraction, Polymorphism, Encapsulation, Inheritence", 
                "created_on": "2017-12-01 07:16:27.722662+00:00", 
                "downvotes": "1", 
                "favorite": false, 
                "id": "533", 
                "in_group": false, 
                "last_modified": "2017-12-01 07:16:27.722689+00:00", 
                "owner": "Suraj Shah", 
                "owner_id": "1", 
                "private": true, 
                "score": "12.431148", 
                "tags": [
                    "java", 
                    "c++", 
                    "oops"
                ], 
                "title": "Tempe Test lorem epsum", 
                "type": "0", 
                "upvotes": "3", 
                "user_owner": true
            }, 
            {
                "content": "Abstraction, Polymorphism, Encapsulation, Inheritence", 
                "created_on": "2017-12-01 06:51:07.536214+00:00", 
                "downvotes": "1", 
                "favorite": false, 
                "id": "532", 
                "in_group": false, 
                "last_modified": "2017-12-01 06:51:07.536242+00:00", 
                "owner": "Suraj Shah", 
                "owner_id": "1", 
                "private": true, 
                "score": "11.086023", 
                "tags": [
                    "java", 
                    "c++", 
                    "oops"
                ], 
                "title": "Tempe Test lorem epsum", 
                "type": "0", 
                "upvotes": "3", 
                "user_owner": true
            }
        ], 
        "status": 200, 
        "success": true
    }
}
"""
