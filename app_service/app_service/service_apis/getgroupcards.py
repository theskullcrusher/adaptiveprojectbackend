"""
Created on 30th Nov '17
@author: surajshah
"""
from flask import Flask, request, session
from flask import current_app as app
from flask.ext import restful

from app_service.conf.config_logger_setup import setup_config_logger
from app_service.service_api_handlers import \
	 get_groupcards_handler
from app_service.utils.resource import Resource
from app_service.utils.auth import get_user

class GetGroupCards(Resource):
	""" 
	This class gets all groupcards
	"""

	def get(self):
		try:
			group = int(request.args.get('group',0))
			return get_groupcards_handler.handle_request(group)        
			close_old_connections()

		except Exception as e:
			app.logger.debug(e)
