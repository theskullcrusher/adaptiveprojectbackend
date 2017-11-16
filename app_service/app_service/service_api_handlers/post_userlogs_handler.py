'''
Created on 15th Nov '17
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

def handle_request(data):
	"""
	  This method logs user activities
	"""
	try:
		user = get_user()
		card = Cards.objects.filter(id=int(data['id'])).first()
		if card == None:
			return {
			'success': True,
			'message': '404 - No such cheatsheet found',
			'status': 404
		}
		UserLogs.objects.create(user=user,card=card,action=data['action'])
		return {
			'success': True,
			'message': 'Successfully logged user activity',
			'status': 200
		}
	except Exception as e:
		app.logger.debug(e)
		return {
		   'success': False, 
		   'errorMessage': 'Internal server error',
		   'errorCode': 500
		}
	finally:
		close_old_connections()
