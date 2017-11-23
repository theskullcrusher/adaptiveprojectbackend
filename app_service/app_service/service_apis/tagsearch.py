"""
Created on 15th Nov '17
@author: surajshah
"""
from flask import Flask, request, session
from flask import current_app as app
from flask.ext import restful

from app_service.conf.config_logger_setup import setup_config_logger
from app_service.service_api_handlers import \
	 get_tagsearch_handler
from app_service.utils.resource import Resource
from app_service.utils.auth import get_user

class TagSearch(Resource):
	""" 
	This class returns tagsearch results
	"""

	def get(self):
		try:
			query = request.args.get('search','')
			return get_tagsearch_handler.handle_request(query)        
			close_old_connections()

		except Exception as e:
			app.logger.debug(e)
