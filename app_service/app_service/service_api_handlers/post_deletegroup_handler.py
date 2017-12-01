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
	  This method deletes a group
	"""
	try:
		user = get_user()

		card = CardGroups.objects.filter(id=int(data['group'])).first()
		if card == None:
			return {
			'success': True,
			'message': '404 - No such group found',
			'status': 404
		}
		if card.owner == user:
			id_ = card.id
			card.delete()
			return {
				'success': True,
				'message': 'Successfully deleted group '+str(id_),
				'status': 200
			}
		return {
			'success': True,
			'message': 'Unauthorized - User is not an owner of group - deletion not allowed',
			'status': 401
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
