'''
Created on 14th Nov '17
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

def handle_request(username, password, details):
	"""
	  This method is used to create a new user and send an 
	  authorization token
	"""
	try:

		if username is None or password is None:
			return {
				'success': False,
				'errorMessage': 'Username/Password cannot be blank',
				'errorCode': 400
			}

		if AppUser.objects.filter(username = username).first() is not None:
			return {
				'success': False,  
				'errorMessage': 'User already exists',
				'errorCode': 400
			}

		user = AppUser.objects.create(username = username,password=password)
		user.refresh_from_db()

#        pdb.set_trace()
		try:
			details_dict = ast.literal_eval(str(details))

			if 'first_name' in details_dict:
				if details_dict['first_name']!= None:
					user.first_name = details_dict['first_name']
					user.save()
				details_dict.pop('first_name',0)

			if 'last_name' in details_dict:
				if details_dict['last_name']!= None:
					user.last_name = details_dict['last_name']
					user.save()
				details_dict.pop('last_name',0)

			# if 'location' in details_dict:
			#     if details_dict['location']!= None:
			#         user.location = details_dict['location']
			#         user.save()
			#     details_dict.pop('location',0)

			user.device_details = json.dumps(details_dict)
			user.save()
						
		except Exception as e:
			app.logger.debug(e)
			app.logger.debug('Exception while storing extra data')

		app.logger.info('User Successfully created')

		return {
			'success': True,
			'content': {
			'username':user.username, 
			 app.auth_header_name: session.get('key')},
			'status': 201
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
