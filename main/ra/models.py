from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User









class Proxies (models.Model):
	proxy = models.CharField(max_length = 100)
	isUsed = models.BooleanField(default = False)

	class Meta:
		db_table = "Proxies"




class Bookmarks (models.Model):
	websiteTitle = models.CharField(max_length = 1000)
	itemType = models.CharField(max_length = 50,null=True)
	url = models.CharField(max_length = 2000,null=True)
	title = models.CharField(max_length = 1000,null=True)
	subtitle = models.CharField(max_length = 1000,null=True)
	author =  models.CharField(max_length = 1000,null=True)
	description =  models.CharField(max_length = 1000,null=True)
	journalItBelongs = models.CharField(max_length = 1000,null=True)
	volume = models.IntegerField(null=True)
	numOfCitation = models.CharField(max_length = 1000, default='')
	numOfDownload = models.CharField(max_length = 1000,default='')
	numOfPages = models.CharField(max_length = 1000, default='')
	edition =models.CharField(max_length = 20,default='')
	publisher = models.CharField(max_length = 1000, default='')
	publicationYear = models.CharField(max_length= 20)
	dateAccessed = models.DateTimeField(default = datetime.now())
	dateAdded = models.DateTimeField(default=datetime.now() )
	DOI = models.CharField(max_length = 200,default='')
	ISSN = models.CharField(max_length = 100,default='')
	isRemoved = models.IntegerField(default = 0)
	user = models.ForeignKey(User, null = False, blank = False, on_delete = models.CASCADE)
	isFavorite = models.BooleanField(default=False)

	class Meta:
		db_table = "Bookmarks"


class Folders (models.Model):
	user = models.ForeignKey(User, null = False, blank = False, on_delete = models.CASCADE)
	parentFolder_id = models.IntegerField(null = True)
	foldername = models.CharField(max_length=25)

	class Meta:
		db_table = "Folders"	


class Bookmark_folders (models.Model):
	user = models.ForeignKey(User, null = False, blank = False, on_delete = models.CASCADE)
	folder = models.ForeignKey(Folders, null = False, blank = False, on_delete = models.CASCADE)
	bookmark = models.ForeignKey(Bookmarks, null = False, blank = False, on_delete = models.CASCADE)

	class Meta:
		db_table = "Bookmark_folders"	





class Headers (models.Model):
	text = models.CharField(max_length = 5000)

	class Meta:
		db_table = "Headers"


class Practice (models.Model):
	text =  models.CharField(max_length = 5)
	time = models.DateTimeField(default=datetime.now())


	class Meta:
		db_table = "Practice"