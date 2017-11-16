'''
Created on 14th Nov '17
@author: surajshah
'''

from flask import Flask, request, session
from flask import current_app as app
from flask.ext import restful

from django.db import close_old_connections
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from app_service.utils.auth import get_user
from app_db.app_models.models import *
import pdb

def handle_request(username, password, remember_me):
	"""
	  This method is used to authorize a user and send an 
	  authorization token
	"""
	try:
		authorized = False

#        pdb.set_trace()
		try:
			user = AppUser.objects.get(username=username)
			if user.password == str(password):
				authorized = True
				session['user_id'] = user.id
				session['password_hash'] = user.password

				if remember_me!= None and int(remember_me)==1:
					session.permanent = True

		except ObjectDoesNotExist:
			authorized = False
			app.logger.debug('User not found')

		if authorized:
			app.logger.info("Validated the login credentials for %s",
							username)
			return {
				'content': {
					'username': user.username,
					app.auth_header_name: session.get('key'),
					'is_authorized': authorized
				},
				'success': True,
				'status' : 200
			}
		else:
			app.logger.exception("Invalid username or password %s",
								 request.remote_addr)
			return {
				'success': False,
				'errorMessage':
					'The email or password you entered is incorrect',
				'errorCode': 403
			}

	except Exception as e:
		app.logger.debug(e)
		return {
			'success': False,
			'errorMessage':
			'Internal Server Error',
			'errorCode': 500
		}
	finally:
		close_old_connections()
	
if __name__ == "__main__":
	print handle_request('ssshah22@asu.edu', 'a', True)
