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
	print response.text
	return response


def populate_db():
	"""Populates the entire database to the given set of input users"""
	users = [['aaa@gmail.com','123'],['bbb@gmail.com','123'],['bbb@gmail.com','123']]






