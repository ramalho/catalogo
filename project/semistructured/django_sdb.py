from __future__ import unicode_literals

from django.db import models

class String(models.CharField):
	def __init__(self, **kwargs):
		kwargs.setdefault('max_length', 1024)
		super(String, self).__init__(**kwargs)
		
Persistent = models.Model
