"""
Created on 15th Nov '17
@author: surajshah
"""
from flask import Flask, request, session
from flask import current_app as app
from flask.ext import restful

from app_service.conf.config_logger_setup import setup_config_logger
from app_service.service_api_handlers import \
	 post_get_cheatsheets_handler
from app_service.utils.resource import Resource
from app_service.utils.auth import get_user

class GetCheatSheets(Resource):
	""" 
	This class gets all cheatsheets
	"""

	def get(self):
		try:
			return post_get_cheatsheets_handler.handle_request()        
			close_old_connections()

		except Exception as e:
			app.logger.debug(e)
