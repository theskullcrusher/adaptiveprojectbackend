"""
Created on 14th Nov '17
@author: surajshah
"""
import django
from os.path import dirname, abspath, join
import os
os.environ["PYTHONPATH"] = os.getcwd()
os.environ["DJANGO_SETTINGS_VARIABLE"] = 'app_db.settings.local'
from django.conf import settings
from django.db import close_old_connections
from flask import Flask
from flask.ext import restful
from app_db.settings.pool import init_pool
from flask.ext.restful import reqparse, abort, Api, Resource
from app_service.conf.config_logger_setup import setup_config_logger
from app_service.session.interfaces import DBInterface
from app_service.service_apis.uservalidation import UserValidation
from app_service.service_apis.usercreation import UserCreation
from app_service.service_apis.getcheatsheets import GetCheatSheets
from app_service.service_apis.updatecheatsheet import UpdateCheatSheet
from app_service.service_apis.createcheatsheet import CreateCheatSheet
from app_service.service_apis.deletecheatsheet import DeleteCheatSheet
from app_service.service_apis.upvote import UpVote
from app_service.service_apis.downvote import DownVote
from app_service.service_apis.favorite import Favorite
from app_service.service_apis.userlogs import UserLogs

from flask.ext.cors import CORS
 
close_old_connections()
django.setup()
init_pool()


app = Flask(__name__)
CORS(app)
app.auth_header_name = 'X-Authorization-Token'
app.session_interface = DBInterface()
app.root_dir = dirname(dirname(abspath(__file__)))
api = restful.Api(app)
setup_config_logger(app)

app.logger.info("Setting up Resources")

api.add_resource(UserCreation, '/userservice/createuser/')
api.add_resource(UserValidation,'/userservice/uservalidation/')
api.add_resource(GetCheatSheets,'/cardservice/getallcards/')
api.add_resource(UpdateCheatSheet,'/cardservice/updatecard/')
api.add_resource(DeleteCheatSheet,'/cardservice/deletecard/')
api.add_resource(CreateCheatSheet,'/cardservice/createcard/')
api.add_resource(UpVote,'/cardservice/upvote/')
api.add_resource(DownVote,'/cardservice/downvote/')
api.add_resource(Favorite,'/cardservice/favorite/')
api.add_resource(UserLogs,'/cardservice/userlogs/')

app.logger.info("Resource setup done")

if __name__ == '__main__':
    from gevent import monkey
    from app_service.utils.hacks import gevent_django_db_hack
    gevent_django_db_hack()
    monkey.patch_all(socket=True, dns=True, time=True, select=True,thread=False, os=True, ssl=True, httplib=False, aggressive=True)
    app.run(host="0.0.0.0",debug=True, port=7285)

