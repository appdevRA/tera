from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User





class Folders (models.Model):
	user = models.ForeignKey(User, null = False, blank = False, on_delete = models.CASCADE)
	parentFolder_id = models.IntegerField(default = 0)
	foldername = models.CharField(max_length=25)

	class Meta:
		db_table = "Folders"	


class Proxies (models.Model):
	proxy = models.CharField(max_length = 100)
	isUsed = models.BooleanField(default = False)

	class Meta:
		db_table = "Proxies"




class Bookmarks (models.Model):
	siteName = models.CharField(max_length = 100)
	user = models.ForeignKey(User, null = False, blank = False, on_delete = models.CASCADE)
	folder = models.ForeignKey(Folders, null = True, blank = True, on_delete = models.CASCADE)
	title = models.CharField(max_length = 500)
	link = models.CharField(max_length = 2000)
	dateAdded = models.DateField(default = datetime.now())
	isRemoved = models.BooleanField(default = False)

	class Meta:
		db_table = "Bookmarks"
