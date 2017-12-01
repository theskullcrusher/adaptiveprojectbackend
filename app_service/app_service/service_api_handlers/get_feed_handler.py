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

def handle_request():
	"""
	  This method returns top 10 most recent feeds
	"""
	try:
		user = get_user()
		result = []
		ulogs = UserLogs.objects.all().order_by('-created_on')
		# if ulogs.count() > 10:
		# 	ulogs = ulogs[:10]
		i_count = 0
		for log in ulogs:
		  if log.card.private == False:
		  	if i_count>=10:
		  		break
			c_dict = {}
			c_dict['timestamp'] = str(log.created_on)
			c_dict['action'] = str(log.action)
			c_dict['id'] = str(log.card.id)
			c_dict['title'] = log.card.title
			c_dict['content'] = log.card.content
			c_dict['upvotes'] = str(log.card.upvotes)
			c_dict['downvotes'] = str(log.card.downvotes)
			c_dict['type'] = str(log.card.c_type)
			c_dict['created_on'] = str(log.card.created_on)
			c_dict['last_modified'] = str(log.card.last_modified)
			c_dict['private'] = log.card.private
			c_dict['in_group'] = log.card.in_group
			fav = Favorite.objects.filter(user=log.user,card=log.card).first()
			if fav == None: 
				c_dict['favorite'] = False
			else:
				c_dict['favorite'] = True
			owner = log.card.owner
			c_dict['owner_id'] = str(owner.id)
			if owner.id == log.user.id:
				c_dict['user_owner'] = True
			else:
				c_dict['user_owner'] = False
			c_dict['owner'] = str(owner.first_name + ' ' +owner.last_name).strip()
			tags = Tags.objects.filter(card=log.card).order_by('-last_modified')
			t_list = []
			for tag in tags:
				t_list.append(str(tag.tag))
			c_dict['tags'] = t_list
			result.append(c_dict)
			i_count += 1

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
