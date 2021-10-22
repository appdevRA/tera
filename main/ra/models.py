from django.db import models
from datetime import datetime
from django.utils import timezone

class User(models.Model):
	username = models.CharField(max_length = 25, null = False)
	password = models.CharField(max_length = 25, null = False)
	proxy = models.CharField(max_length = 40, null = True)


	class Meta:
		db_table = "User"

class Articles (models.Model):
	title = models.CharField(max_length = 100)
	author = models.CharField(max_length = 50)
	date_uploaded = models.DateField(auto_now=True)
	file = models.FileField(upload_to='articles/')

	reftype = models.CharField(max_length = 25, null = False)

	class Meta:
		db_table = "Articles"



class Folders (models.Model):
	foldername = models.CharField(max_length=25)
	user = models.ForeignKey('User',on_delete=models.CASCADE, null = True)

	class Meta:
		db_table = "Folders"	


class Proxies (models.Model):
	proxy = models.CharField(max_length = 100)
	isUsed = models.IntegerField( default = 0)

	class Meta:
		db_table = "Proxies"


class Bookmarks (models.Model):
	user = models.ForeignKey(User, null = False, blank = False, on_delete = models.CASCADE, related_name = "User")
	link = models.CharField(max_length = 500)
	dateAdded = models.DateField(default = datetime.now())
	isRemoved = models.BooleanField(default = False)

	class Meta:
		db_table = "Bookmarks"
