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
from itertools import chain

def handle_request():
	"""
	  This method returns all groups
	"""
	try:
		user = get_user()
		result = []

		groups = GroupsUser.objects.filter(user=user).distinct()		

		for ugroup in groups:
			c_dict = {}
			c_dict['id'] = str(ugroup.group.id)
			c_dict['title'] = str(ugroup.group.title)
			c_dict['created_on'] = str(ugroup.group.created_on)
			c_dict['last_modified'] = str(ugroup.group.last_modified)
			owner = ugroup.group.owner
			c_dict['owner_id'] = str(owner.id)
			if owner.id == user.id:
				c_dict['user_owner'] = True
			else:
				c_dict['user_owner'] = False
			c_dict['owner'] = str(owner.first_name + ' ' +owner.last_name).strip()
			result.append(c_dict)

		return {
			'success': True,
			'result': result.reverse(),
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
