'''
Created on 23th Nov '17
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
from app_service.utils.user_accounts_utils import search_index_para
import traceback

def handle_request(query):
	"""
	  This method returns tagsearch results
	"""
	try:
		user = get_user()
		result = []

		response = search_index_para(query,"tags")

		val = [doc['_id'] for doc in response['hits']['hits']]
		scores = [doc['_score'] for doc in response['hits']['hits']]
		for z, v in enumerate(val):
			card = Cards.objects.filter(id=int(v)).first()
			if card is not None:
				c_dict = {}
				c_dict['score'] = str(scores[z])
				c_dict['id'] = str(card.id)
				c_dict['title'] = card.title
				c_dict['content'] = card.content
				c_dict['upvotes'] = str(card.upvotes)
				c_dict['downvotes'] = str(card.downvotes)
				c_dict['type'] = str(card.c_type)
				c_dict['created_on'] = str(card.created_on)
				c_dict['last_modified'] = str(card.last_modified)
				fav = Favorite.objects.filter(user=user,card=card).first()
				if fav == None: 
					c_dict['favorite'] = False
				else:
					c_dict['favorite'] = True
				owner = card.owner
                                c_dict['owner_id'] = str(owner.id)
                                if owner.id == user.id:
                                        c_dict['user_owner'] = True
                                else:
                                        c_dict['user_owner'] = False
				c_dict['owner'] = str(owner.first_name + ' ' +owner.last_name).strip()
				tags = Tags.objects.filter(card=card).order_by('-last_modified')
				t_list = []
				for tag in tags:
					t_list.append(str(tag.tag))
				c_dict['tags'] = t_list
				result.append(c_dict)

		return {
			'success': True,
			'result': result,
			'status': 200
		}
	except Exception as e:
		traceback.print_exc()
		app.logger.debug(e)
		return {
		   'success': False, 
		   'errorMessage': 'Internal server error',
		   'errorCode': 500
		}
	finally:
		close_old_connections()
