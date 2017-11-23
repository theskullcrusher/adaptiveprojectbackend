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
from app_service.utils.user_accounts_utils import update_index

def handle_request(data):
	"""
	  This method updates a cheatsheet
	"""
	try:
		user = get_user()
		tags = data['tags']
		card = Cards.objects.filter(id=int(data['id'])).first()
		if card == None:
			return {
				'success': True,
				'message': '404 - No such cheatsheet found',
				'status': 404
			}
		if card.owner != user:
			return {
				'success': True,
				'message': 'Unauthorized - User needed to be the owner of cheatsheet to update it',
				'status': 401
			}

		card.title = data['title']
		card.content = data['content']
		card.c_type = int(data['type'])
		card.save()
		if len(tags) != 0:
			Tags.objects.filter(card=card).delete()
			for each in tags:
				Tags.objects.create(card=card,tag=str(each))

		data['id'] = card.id
		flg = update_index(data)
		return {
			'success': True,
			'message': 'Successfully updated cheatsheet and updated ES: '+str(flg),
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
