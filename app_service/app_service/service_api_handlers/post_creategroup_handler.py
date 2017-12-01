'''
Created on 30th Nov '17
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
	  This method returns creates a new group
	"""
	try:
		user = get_user()

		group = CardGroups.objects.create(owner=user,title=data['title'])
		guser = GroupsUser.objects.create(user=user,group=group)
		return {
			'success': True,
			'message': 'Successfully created group',
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
