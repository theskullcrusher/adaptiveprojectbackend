'''
Created on 29th Nov '17
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
from itertools import chain

def handle_request(group):
	"""
	  This method returns groups users or all users
	"""
	try:
		user = get_user()
		result = []
		if group == 0:
			allusers = AppUser.objects.all()
		else:
			gp = CardGroups.objects.filter(id=group).first()
			if gp != None:
				allusers = GroupsUser.objects.filter(group=gp)
				allusers = [x.user for x in allusers]
			else:
				allusers = []

		for each in allusers:
			c_dict = {}
			c_dict['id'] = str(each.id)
			c_dict['name'] = str(each.first_name + ' ' +each.last_name).strip()
			c_dict['email'] = str(each.email)
			result.append(c_dict)

		return {
			'success': True,
			'result': result,
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
