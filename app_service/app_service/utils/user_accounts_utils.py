'''
Created on 21st Nov '17
@author: surajshah
'''

from flask import Flask, request, session
from flask import current_app as app
from flask.ext import restful

from django import db
from django.db import close_old_connections
from django.contrib.auth.models import User
from app_service.utils.auth import get_user
from app_db.app_models.models import *
import ast
import json
import pdb
import requests, json
from elasticsearch import Elasticsearch
import pprint


def search_index_main(search):
	"""Search an index"""
	es = Elasticsearch()
	body = {"query": {"multi_match": {"query":search, "fields":["content","title","tags"]}}
	}
	res = es.search(index='cheatsheets',body=body)	
	pp = pprint.PrettyPrinter(indent=4)
	#pp.pprint(res)
	return res


def search_index_para(search, key):
	"""Search an index"""
	es = Elasticsearch()
	body = {"query": {"match": {key:search}}
	}
	res = es.search(index='cheatsheets',body=body)	
	pp = pprint.PrettyPrinter(indent=4)
	#pp.pprint(res)
	return res


def create_index(data):
	"""Used to create index, etc"""
	es = Elasticsearch()
	try:
		res = es.index(index='cheatsheets', doc_type='cards', body=data, op_type='create', id=int(data['id']))
		return True
	except Exception as e:
		print e
		return False	

def delete_index(id_):
	"""Used to delete index, etc"""
	es = Elasticsearch()
	try:
		res = es.delete(index='cheatsheets', doc_type='cards',  id=int(id_))
		return True
	except Exception as e:
		print e
		return False	

def update_index(data):
	"""Used to update index, etc"""
	es = Elasticsearch()
	try:
		res = es.update(index='cheatsheets', doc_type='cards', body={"doc":data}, id=int(data['id']))
		return True
	except Exception as e:
		print e
		return False	


def create_user(data):
	# data = {'email':'aaa@gmail.com','pswd':'123','details':{'first_name':'AAA','last_name':'User 1'}} # "X-Authorization-Token": "089b2d64-1c0f-4457-85dc-7060e3f5fdc7"
	# data = {'email':'bbb@gmail.com','pswd':'123','details':{'first_name':'BBB','last_name':'User 2'}} #  "X-Authorization-Token": "e46cc17e-cc4b-49e6-a7f5-bd9fe387beea"
	# data = {'email':'ccc@gmail.com','pswd':'123','details':{'first_name':'CCC','last_name':'User 3'}} # "X-Authorization-Token": "c8bdd3b0-2277-4462-ba1d-f7a3d02da9e9"
	headers = {'content-type':'application/json'}
	url = 'http://ec2-18-221-144-47.us-east-2.compute.amazonaws.com/userservice/createuser/'
	response = requests.post(url,headers=headers,data=json.dumps(data))
	print response.text
	return response


def login_user(email, pswd):
	data = {'email':email,'pswd':pswd,'remember_me':'1'} 
	headers = {'content-type':'application/json'}
	url = 'http://ec2-18-221-144-47.us-east-2.compute.amazonaws.com/userservice/uservalidation/'
	response = requests.post(url,headers=headers,data=json.dumps(data))
	#print response.text
	return response


def populate_db():
	"""Populates the entire database to the given set of input users"""
	#Delete all current data:
	users = [['aaa@gmail.com','123'],['bbb@gmail.com','123'],['ccc@gmail.com','123']]
	count = len(users)
	data = {}
	with open('card_data/cards.json','r') as f:
		data = json.load(f)

	data_list = []
	start = 0
	for i in xrange(count):
		end = (i+1)*len(data)/count
		data_list.append(data[start:end])
		start = end
	for n, each in enumerate(users):
		data = data_list[n]
		key = login_user(each[0],each[1]).json()['responseData']['content']['X-Authorization-Token']

		headers = {'content-type':'application/json', 'Origin':['POST','PUT','DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH'], 'X-Authorization-Token': key}
		url = 'http://ec2-18-221-144-47.us-east-2.compute.amazonaws.com/cardservice/createcard/'

		for d in data:
			da = {}
			da['title'] = d['title']
			da['content'] = d['content']
			da['tags'] = d['tags']
			da['type'] = d['type']
			da['upVote'] = str(d['upVote'])
			da['downVote'] = str(d['downVote'])

			response = requests.post(url,headers=headers,data=json.dumps(da))
			if response.status_code != 200:
				print response.text

	print "Successfully populated all users"


if __name__ == "__main__":
	populate_db()
