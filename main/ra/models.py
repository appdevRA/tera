from django.db import models
from datetime import datetime
from django.utils import timezone

class User(models.Model):
	username = models.CharField(max_length = 25, null = False)
	password = models.CharField(max_length = 25, null = False)

	class Meta:
		db_table = "User"

class Articles (models.Model):
	title = models.CharField(max_length = 100)
	author = models.CharField(max_length = 50)
	file = models.FileField(upload_to='articles/')
	reftype = models.CharField(max_length = 25, null = False)

	class Meta:
		db_table = "Articles"

class Citations (models.Model):
	contributor = models.CharField(max_length=25)
	fname = models.CharField(max_length=25)
	minitial = models.CharField(max_length=5)
	lname = models.CharField(max_length=25)
	ar_title = models.CharField(max_length=100)
	jour_title = models.CharField(max_length=100)
	volume = models.IntegerField()		
	issue = models.IntegerField()
	series = models.IntegerField()
	pubdate = models.DateField(default = datetime.now())
	pagestart = models.IntegerField()
	pagend = models.IntegerField()
	annotation = models.CharField(max_length=100)
	referencetype = models.CharField(max_length=25)
	citationformat = models.CharField (max_length=15)

	class Meta:
		db_table = "Citations"

class Folders (models.Model):
	foldername = models.CharField(max_length=25)

	class Meta:
		db_table = "Folders"		