"""
Created on 30th Nov '17
@author: surajshah
"""
from flask import Flask, request, session
from flask import current_app as app
from flask.ext import restful

from app_service.conf.config_logger_setup import setup_config_logger
from app_service.service_api_handlers import \
	 post_deletegroup_handler
from app_service.utils.resource import Resource
from app_service.utils.auth import get_user

class DeleteGroup(Resource):
	""" 
	This class deletes a group
	"""

	def post(self):
		try:
			data = request.get_json(force=True)
			app.logger.debug("Call to delete group:"+str(data))

			return post_deletegroup_handler.handle_request(data)        
			close_old_connections()

		except Exception as e:
			app.logger.debug(e)