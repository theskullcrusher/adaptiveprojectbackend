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
from app_service.utils.user_accounts_utils import create_index

def handle_request(data):
	"""
	  This method adds user to group
	"""
	try:
		user = get_user()
		gp = data['group']
		group = CardGroups.objects.filter(id=int(gp)).first()
		usrs = data['users']
		usrs = [int(x) for x in usrs]
		addusers = AppUser.objects.filter(id__in=usrs)
		for each in addusers:
			GroupsUser.objects.create(group=group,user=each)
		return {
			'success': True,
			'message': 'Successfully added users to groups',
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
