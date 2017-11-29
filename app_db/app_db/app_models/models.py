from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.postgres.fields import ArrayField
from jsonfield import JSONField
from time import time
import sys, os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app_db.settings.local")
# from datetime import datetime
# import django
# import traceback
# django.setup()
# from mwd_proj.utils.utils2 import *
# import traceback
# from django.db.models import Sum
# import operator
# import math
# from django.db.models.functions import Lower
# from django.db.models import Q

class AppUser(User):
	summary = models.TextField(blank=True)
	other_details = JSONField(blank=True, null=True)
	created_on = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)


class Cards(models.Model):
	owner = models.ForeignKey('AppUser')
	title = models.TextField(blank=True)
	content = models.TextField(blank=True)
	upvotes = models.IntegerField(default=0)
	downvotes = models.IntegerField(default=0)
	c_type = models.IntegerField(default=0)
	created_on = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)
	private = models.BooleanField(default=False)


class Tags(models.Model):
	card = models.ForeignKey('Cards')
	tag = models.TextField(blank=True)
	created_on = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)


class Favorite(models.Model):
	user = models.ForeignKey('AppUser')
	card = models.ForeignKey('Cards')
	created_on = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)


class UserLogs(models.Model):
	user = models.ForeignKey('AppUser')
	card = models.ForeignKey('Cards')
	action = models.TextField(blank=True)
	created_on = models.DateTimeField(auto_now_add=True)
