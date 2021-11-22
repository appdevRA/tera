from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractUser



class Department (models.Model):
	abbv = models.CharField(max_length=50, null = False, blank= False, default='')
	name = models.CharField(max_length=200, null = False, blank= False)
	class Meta:
		db_table = "Department"

class User (AbstractUser):

	department= models.ForeignKey(Department, null = False, blank = False, on_delete = models.CASCADE)

	REQUIRED_FIELDS = ['first_name', 'last_name','department','password']
	class Meta:
		db_table = "User"


class Admin (models.Model):
	user = models.ForeignKey(User, null = False, blank = False, on_delete = models.CASCADE)
	department_id= models.ForeignKey(Department, null = False, blank = False, on_delete = models.CASCADE)
	class Meta:
		db_table = "Admin"



class User_bookmark (models.Model):
	websiteTitle = models.CharField(max_length = 1000, null = False)
	itemType = models.CharField(max_length = 50,null=False)
	url = models.CharField(max_length = 2000,null=False)
	title = models.CharField(max_length = 1000,null=False)
	subtitle = models.CharField(max_length = 1000,null=True)
	author =  models.CharField(max_length = 1000,blank= True)
	description =  models.CharField(max_length = 1000,blank= True)
	journalItBelongs = models.CharField(max_length = 1000,blank= True)
	volume = models.IntegerField(blank= True)
	numOfCitation = models.CharField(max_length = 1000,blank= True)
	numOfDownload = models.CharField(max_length = 1000,blank= True)
	numOfPages = models.CharField(max_length = 1000,blank= True)
	edition =models.CharField(max_length = 20,blank= True)
	publisher = models.CharField(max_length = 1000, blank= True)
	publicationYear = models.CharField(max_length= 20,blank= True)
	dateAccessed = models.DateTimeField(default = datetime.now())
	dateAdded = models.DateTimeField(default=datetime.now() )
	DOI = models.CharField(max_length = 200,blank= True)
	ISSN = models.CharField(max_length = 100,blank= True)
	isRemoved = models.IntegerField(default = 0)
	user = models.ForeignKey(User, null = False, blank = False, on_delete = models.CASCADE)
	isFavorite = models.BooleanField(default=False)
	date_removed = models.DateTimeField(blank = True, null = True)

	class Meta:
		db_table = "User_bookmark"

class Dissertation(models.Model):
	title = models.CharField(max_length=1000)
	abstract = models.CharField(max_length=2000)

	class Meta:
		db_table = "Dissertation"

class Dissertation_authors(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=30)
	dissertation = models.ForeignKey(Dissertation, null = False, blank = False, on_delete = models.CASCADE)

	class Meta:
		db_table = "Dissertation_authors"


class User_file(models.Model):
	user = models.ForeignKey(User, null = False, blank = False, on_delete = models.CASCADE)
	file = models.FileField(upload_to ='media', null = False)
	class Meta:
		db_table = "User_files"


class Group(models.Model):
	name = models.CharField(max_length=50) #add not null and not blank here
	description = models.CharField(max_length=200)
	owner = models.ForeignKey(User, null = False, blank = False, on_delete = models.CASCADE)
	date_created = models.DateTimeField(default=datetime.now())
	class Meta:
		db_table = "Group"

class Group_member(models.Model):
	group = models.ForeignKey(Group, null = False, blank = False, on_delete = models.CASCADE)
	user = models.ForeignKey(User, null = False, blank = False, on_delete = models.CASCADE)
	class Meta:
		db_table = "Group_member"

class Group_bookmark(models.Model):
	group =models.ForeignKey(Group, null = False, blank = False, on_delete = models.CASCADE)
	bookmark = models.ForeignKey(User_bookmark, null = False, blank = False, on_delete = models.CASCADE)
	added_by = models.ForeignKey(User, null = False, blank = False, on_delete = models.CASCADE)
	date_added = models.DateTimeField(default=datetime.now())
	is_removed = models.IntegerField(default=0)
	date_removed = models.DateTimeField(blank=True,null = True)

	class Meta:
		db_table = "Group_bookmark"


class Folder(models.Model):
	name = models.CharField(max_length=25, unique=True)
	user = models.ForeignKey(User, null = False, blank = False, on_delete = models.CASCADE, default=None)
	date_created = models.DateTimeField(default=datetime.now())

	class Meta:
		db_table = "Folder"	

class Bookmark_folder (models.Model):
	user = models.ForeignKey(User, null = False, blank = False, on_delete = models.CASCADE)
	folder = models.ForeignKey(Folder, null = False, blank = False, on_delete = models.CASCADE)
	bookmark = models.ForeignKey(User_bookmark, null = False, blank = False, on_delete = models.CASCADE)
	date_added = models.DateTimeField(default=datetime.now())
	is_removed = models.IntegerField(default=0)
	date_removed = models.DateTimeField(blank=True,null = True)

	class Meta:
		db_table = "Bookmark_folder"	


	


	



class Site (models.Model):
	name = models.CharField(max_length= 100)
	url= models.CharField(max_length= 300)
	added_by = models.ForeignKey(Admin, null = False, blank = False, on_delete = models.DO_NOTHING)
	date_added = models.DateTimeField(default=datetime.now())

	class Meta:
		db_table = "Site"	


class User_access (models.Model):
	user = models.ForeignKey(User, null = False, blank = False, on_delete = models.CASCADE)
	department = models.ForeignKey(Department, null = False, blank = False, on_delete = models.CASCADE)
	site = models.ForeignKey(Site, null = False, blank = False, on_delete = models.CASCADE)
	date_of_access = models.DateTimeField(default=datetime.now())

	class Meta:
		db_table = "User_access"	


class Headers (models.Model):
	text = models.CharField(max_length = 5000)

	class Meta:
		db_table = "Headers"


class Practice (models.Model):
	text =  models.CharField(max_length = 5)
	time = models.DateTimeField(default=datetime.now())


	class Meta:
		db_table = "Practice"



class Proxies (models.Model):
	proxy = models.CharField(max_length = 100)
	isUsed = models.BooleanField(default = False)

	class Meta:
		db_table = "Proxies"
