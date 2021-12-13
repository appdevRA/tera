from django.http import Http404
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.utils import timezone
from .forms import *

from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.core import serializers
from django.db import connection
from django.db.models import Q, Count

from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from . import serializers
from .links import *
from .models import *
import ast
import json
from bs4 import BeautifulSoup
from .links import *
import requests
import csv
import io
class adminIndexView(View):
	def get(self, request):
		print('olok')
		
		return render(request,'adminIndex.html')

class practice2(View):
	def get(self, request, sinput, site,type):
		print('olok')
		
		return HttpResponse(sinput +" "+site+" "+type)

class addUser(View):
	def get(self, request):
		print('olok')
		
		return render(request,'addUser.html')

		

class practice3(View):
	
	def get(self, request):
		return HttpResponse(self.a)
	def post(self, request):
		if request.method == 'POST' and request.is_ajax():
			print('practice 3 post')

			
			return HttpResponse(request.GET.get('search'))

class practice(View):
	
	def get(self, request):
		# userBbookmarks= User_bookmark.objects.filter(user=request.user).values('title')
		# recommendation = []
		
		# if userBbookmarks.exists():
		# 	queryAll= list(User_bookmark.objects.values('id','title','user_id')
		# 										.annotate(folder_count=Count('folders'))
		# 										.order_by("-folder_count"))#"id","title","user",))


		queryAll = User.objects.select_related('User_bookmark').filter(id=2).values("user_bookmark__title","first_name","user_bookmark__keyword").all() # this retrieves all records
		# print(a)
		for a in queryAll:
			print(a)
			# a = modes(queryAll, request.user.id).to_dict("records") 

			# for b in a:
			# 	print(b)

			# a = User_bookmark.objects.annotate(id=1)
			# print("folders count: ",a.folders.all().count())
			# print("recommended","\n",a )
			# recommendation = list(dict.fromkeys(modes(queryAll, request.user.id) ))
		
		# a= Department.objects.create(name='College of Computer Studies', abbv='CCS')
		# User.objects.create(username='18-5126-269', password =make_password('12345'), department=a)


		# User.objects.create(username='18-5126-270', password =make_password('12345'), department=a)

		# User.objects.create(username='mondejar2', password = make_password('mondejar.12345'), department_id=2)
		

		# cursor = connection.cursor()   
		#datetime.now().month = #get month of current time
		# cursor.execute("SELECT b.isRemoved, COUNT(b.user_id) FROM auth_user u, bookmarks b WHERE u.id=b.user_id AND b.dateAdded LIKE '2021-11%' GROUP BY isRemoved") #| get rows of for a specific date|
		# cursor.execute("SELECT user_id, COUNT(user_id) AS `value_occurrence` FROM Bookmarks GROUP BY user_id ORDER BY `value_occurrence` DESC LIMIT 1") # |get the most frequent user ID (top1 ky limit 1 man)|
		# cursor.execute("Select b.* from Bookmarks b, bookmark_folders bf Where bf.user_id = "+str(request.user.id)+" AND bf.folder_id = "+ str(1)+" AND bf.bookmark_id = b.id"  ) #|for retrievving bookmarks inside a folder|
		# row = cursor.fetchall()
		
		# queryset = User.objects.filter(id = Bookmarks.objects.filter(dateAdded__contains='2021-11-17').values('user_id'))   #| get rows of for a specific date|
		# row = cursor.fetchall()
		# print()

		# cursor.execute("SELECT id, COUNT(id) FROM Bookmarks GROUP BY dateAdded LIKE '2021-11%'") # |get the most frequent user ID (top1 ky limit 1 man)|
		# row = cursor.fetchall()
		# print(row)
		# queryset = User_bookmark.objects.all()
		# a = list(queryset)
		# context = {
		#     "bookmark_set": queryset,
		#     # "bookmark_list" : a 
		# }
		# return HttpResponse()


		# OTL('war', 1232, 'Text book', 1)
		# a = OER('animals', 'proxy', 'Text book', 2)
		# for b in a:
		# 	print(b['title'])
		# a= OER('peace', 'Text book', 1)

		
		return render(request,'practice.html')#,context)

	def post(self, request):
		
		
		myfile = request.FILES['file']
		print(type(myfile))
		file = myfile.read().decode('utf-8')
		dict_reader = csv.DictReader(io.StringIO(file))

		# a_csv_file = open(a,'r')
		# dict_reader = csv.DictReader(a_csv_file)
		print(list(dict_reader))
		# for i, a in enumerate(list(dict_reader)):
		# 	ordered_dict_from_csv = a
		# 	row = dict(ordered_dict_from_csv)
		# 	print(a)

			# user = User(
			# 	username = row['username'], 
			# 	password=make_password(row['password']),
			# 	first_name= row['first_name'], 
			# 	last_name=row['last_name'], 
			# 	department =  Department.objects.get(abbv=row['department'])
			# 	)
			# try:
			# 	user.save()
			# except Exception as e:
			# 	print(str(e).replace("(","").replace(")",""), "at line ", i+2)
			
		return HttpResponse('practice post')
		
			
		
		


class TeraLoginUser(View): 

	def get(self,request):
		# proxies = proxy_generator2() #/ generating free proxies /
		# for proxy in proxies:  #/ saving proxies to db /
			
		# 	proxy = Proxies(proxy = proxy)
		# 	proxy.save()
		
		if( request.user.id != None):
			try:
				return redirect("ra:" + request.session.get('previousPage'))
			except:
				request.session['previousPage'] = 'index_view'
				return redirect("ra:index_view")
		else:
			
			return render(request,'login.html')	
		
		

	def post(self, request):
		
	
		
		if 'buttonlogin' in request.POST:
			print('Login Button CLiked!')
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)

				if request.session.get('previousPage') == None:
					return redirect("ra:index_view")
				else:
					return redirect('ra:'+ request.session.get('previousPage'))
			else:
				messages.success(request, "Invalid Username or password")
				return redirect('ra:tera_login_view')
				
				
		
		
					
		
		 
			
class TeraIndexView(View):
	def get(self, request):
		# User_bookmark.objects.exclude(id=6).delete()
		# logout(request)
		#proxies = proxy_generator2() #/ generating free proxies /
		#for proxy in proxies:  #/ saving proxies to db /
			
		#	proxy =Proxies(proxy = proxy)
		#	proxy.save()
		
		

		request.session['previousPage'] = 'index_view'
		
		context ={
			"user":request.user.is_authenticated
		}
		
	
		
		#x = Proxies.objects.filter(id = proxyID.id).update(isUsed = 1)
		return render(request,'landingpage.html',context)

	def post(self, request):

		if 'buttonLogin' in request.POST:
			request.session['previousPage'] = request.POST['previousPage']
			print(request.session.get('previousPage'))
			return redirect('ra:tera_login_view')

		elif 'btnLogout' in request.POST:
			proxy = request.session.get('proxy')

			logout(request)

			request.session['proxy'] = proxy
			return redirect("ra:index_view")

		elif 'btnSearch' in request.POST:
			request.session['word'] = request.POST.get("keyword")
			
			return redirect('ra:search_result_view')
		


class TeraSearchResultsView(View):
	

	def get(self,request):
		request.session['previousPage'] ='search_result_view'
		# header = ast.literal_eval(Headers.objects.get(id=2).text)	# converting from string to dictionary
		# header = request.session.get('header')
		word = request.session.get('word')

		

		if request.session.get('website') != None:
			website = request.session.get('website')
		else:
			website = "Springeropen"

		if request.session.get('itemType') != None:
			itemType = request.session.get('itemType')
		else:
			itemType = "article"
						
		context = {
							'keyword': word,
							'isGet': 0,
							'website': website,
							'itemType': itemType,
							'is_authenticated': str(request.user.is_authenticated)
		}
		
		return render(request,'searchresults.html', context)

	def post(self, request):
		
		if request.method == 'POST' and request.is_ajax():
			
			
			
			action = request.POST['action']

			if action == "search":
				
				print("is get? "+ request.POST['isGet'])
				# print(type(request.POST['isGet']))
				# print("search")
				# if isGet == True:
				# else:
					# User_acces.objects.create()
				word = request.POST['word']
				request.session['word'] = word
				

				website = request.POST['site']
				itemType = request.POST['itemType']
				request.session['website'] =website
				request.session['itemType'] = itemType


				a = scrape(word,itemType , website,' ', request.POST['pageNumber'])

				results = a	
				
				print(len(results))
				context = {
					'results': results,
					'is_authenticated': request.user.is_authenticated,
					"isGet": False
				}
				return JsonResponse(context)
					
			elif action == "add":
				print('bookmark button clicked')
				keyword = request.POST['word']
				bookmark = request.POST['bookmark']
				siteRef = request.POST['website'] +" " +request.POST['reftype']
				string = bookmark.split('||')
				title = string[0].replace('\n','').replace('  ','')
				url = string[1]
				# print(title, url, siteRef)
				detail = details(url, request.session.get('proxy'),siteRef)

				websiteTitle = detail['websiteTitle']
				itemType = detail['itemType']
				author = detail['author']
				description = detail['description']
				journalItBelongs = detail['journalItBelongs']
				volume = detail['volume']
				doi = detail['doi']
				publicationYear = detail['publishYear']
				subtitle = detail['subtitle']
				citation = detail['citation']
				downloads = detail['downloads']
				publisher = detail['publisher']
				edition = detail['edition']
				pages = detail['pages']
				# author description publication volume doi
				
				
				# print(websiteTitle + '\n'+itemType + '\n'+title + '\n' +link + '\n' +author+ '\n' +description+ '\n' +publication+ '\n' +volume+ '\n' +doi)
				if request.POST['reftype'] == "article":
					detail = Bookmark_detail.objects.create(
						title = title,websiteTitle= websiteTitle,itemType= itemType,
						author = author, description= description, url = url, journalItBelongs= journalItBelongs, 
						volume = volume, DOI = doi
						)
					Bookmark.objects.create(user = request.user,bookmark=detail,keyword=keyword)
					
					
				elif itemType == "book":
					detail = Bookmark_detail.objects.create(title = title,websiteTitle= websiteTitle,
						subtitle = subtitle, itemType= itemType,author = author,numOfCitation = citation,
						numOfDownload= downloads,publisher=publisher, description= description, url = url, 
						edition = edition,numOfPages = pages, DOI = doi)

					Bookmark.objects.create(user = request.user,bookmark=detail,keyword=keyword)
				return HttpResponse('')
			else:
				string = bookmark.split('||')

				title = string[1].replace('\n','').replace('  ','')
				User_bookmark.objects.filter(title=title).update(isRemoved=1)
				return HttpResponse('')

		elif 'buttonLogin' in request.POST:
			request.session['previousPage'] = request.POST['previousPage']
			print(request.session.get('previousPage'))
			return redirect('ra:tera_login_view')

		elif 'btnLogout' in request.POST:
			word = request.session.get('word')
			proxy = request.session.get('proxy')
			pp = request.session.get('previousPage')

			logout(request)
			request.session['previousPage'] = pp
			request.session['word'] = word
			request.session['proxy'] = proxy

			return redirect("ra:search_result_view")
			


		

		

class TeraDashboardView(View):

	def get(self,request):
		# Department.objects.create(abbv='CCS', name="College of Computer Studies")
		# Group.objects.get(id=1).member.add(User.objects.get(username='mondejars'))
		#.distinct()
		
		
		# Folder.objects.all().delete()
		# User_bookmark.objects.all().delete()
		request.session['previousPage'] = "tera_dashboard_view"
		# try:
			# cursor = connection.cursor()   
			# cursor.execute("SELECT f.*, b.* FROM User_bookmark b, Folders f WHERE f.user_id = "+ request.user.id+" AND f.bookmark_id == b.id OR") #| get rows of for a specific date|
			# row = cursor.fetchall()




		if request.user.id != None:





			# userBookmarks= User_bookmark.objects.filter(user=request.user).values('title')
			# recommendation = []
			
			# # if userBookmarks.exists():
			# # 	queryAll= list(User_bookmark.objects.values('id','title','user_id')
			# # 										.annotate(folder_count=Count('folders'))
			# # 										.order_by("-folder_count"))
			# # recommendation = modes(queryAll, request.user.id).to_dict("records") 												

			
			
			# query_group = Group.objects.filter((Q(owner= request.user) | Q(member=request.user)), is_removed=0)
			# groups = list(query_group.values())
			# for b in groups:
			# 	b['owner_id']= list(User.objects.filter(id=b['owner_id']).values('first_name',"last_name"))
			# 	c = User_group.objects.get(id=b['id'])
			# 	b['members']= list(c.member.values('first_name','last_name'))

			


			
			# 	print(b['owner_id'])
			# cursor = connection.cursor()   
			# cursor.execute()
			# a = dictfetchall(cursor)
			# a = json.dumps(a, default=str)
			queryset = Bookmark.objects.select_related("bookmark").filter(
																		( Q(user=request.user) ) & 
																		( Q(isRemoved=1) | Q(isRemoved=0) ), 
																		folder= None, group = None
																		).values(
																			"id", "bookmark__id", "isFavorite", "dateAccessed", "dateAdded", 
																			"isRemoved", "date_removed",
																			"bookmark__websiteTitle", "bookmark__itemType",
																			"bookmark__url", "bookmark__title", "bookmark__subtitle",
																			"bookmark__subtitle", "bookmark__author", "bookmark__description",
																			"bookmark__journalItBelongs", "bookmark__volume",
																			"bookmark__numOfCitation", "bookmark__numOfPages",
																			"bookmark__publisher", "bookmark__publicationYear",
																			"bookmark__DOI", "bookmark__ISSN", "bookmark__edition", "bookmark__numOfDownload"
																				).distinct()
											



                

			# print(queryset)
			# return HttpResponse("olok")

			# queryset = User_bookmark.objects.filter((Q(user_id=request.user.id) | Q(folders__user=request.user)) &  (Q(isRemoved=1) | Q(isRemoved=0))).distinct().values()
			# print(len(queryset))
			folders =	Folder.objects.filter(user_id=request.user, is_removed = 0).values()
			# groups = Group.objects.filter(Q(owner= request.user) | Q(member=request.user), is_removed=0).distinct().values()
			groups= Group.objects.select_related("member").filter((Q(owner= request.user) | Q(member=request.user)),
																			 is_removed=0).values(
																			 						"id","name", "date_created",
																			 						"owner__first_name",
																			 						"owner__last_name",
																			 						"member__first_name",
																			 						"member__last_name")

			a = json.dumps(list(queryset), default=str)
			folder_list = json.dumps(list(folders), default=str)
			group_list = json.dumps(list(groups), default=str)

			context = {
				"bookmark_list": a,
				# "folder_set": folders,
			    "folder_list": folder_list,
			    "group_list":group_list,
			    # "recommendation": recommendation
			}
			return render(request,'collections.html', context)
		else:
			return redirect('ra:tera_login_view')

		# except:
		# 	request.session['previousPage'] = 'tera_dashboard_view'
		# 	return redirect('ra:tera_login_view')

	def post(self, request):

	 	# form = CreateFolderForm(request.POST)

		if 'btnLogout' in request.POST:
			word = request.session.get('word')
			prevPage = request.session.get('previousPage')
			proxy = request.session.get('proxy')

			logout(request)

			request.session['word'] = word
			request.session['previousPage'] = prevPage
			request.session['proxy'] = proxy

			return redirect("ra:" + request.session.get('previousPage'))

		

		elif request.method == 'POST' and request.is_ajax():
				
			action = request.POST['action']

			
			if action == 'addFav':
				Bookmark.objects.filter(bookmark_id=request.POST['bID'], user= request.user, group = None).update(isFavorite=1)
				return HttpResponse('')
			elif action == 'remFav':
				Bookmark.objects.filter(bookmark_id=request.POST['bID'], user= request.user, group = None).update(isFavorite=0)
				return HttpResponse('')
			elif action == 'trashItem':
				Bookmark.objects.filter(bookmark_id=request.POST['bID'], user= request.user, group = None).update(isRemoved=1, date_removed= timezone.now())
				# print('len of trash item', Bookmark.objects.filter(bookmark_id=request.POST['bID'], user= request.user).count())
				return HttpResponse('')
			elif action == 'unTrashItem':
				Bookmark.objects.filter(bookmark_id=request.POST['bID'], user= request.user, group = None).update(isRemoved=0,date_removed= None)
				return HttpResponse('')
			elif action == 'deleteItem':
				Bookmark.objects.filter(bookmark_id=request.POST['bID'], user= request.user, group = None).update(isRemoved=2, date_removed= timezone.now())
				return HttpResponse('')

			elif action == 'add_bookmark_to_faction':
				factionID = request.POST['faction_id']
				bdID = request.POST['bID']
				faction = request.POST['faction']
				
				if faction =="folder":
					print('yes folder')
					if Bookmark.objects.filter(folder__id= factionID,bookmark__id=bdID, isRemoved=0).exists():
						return HttpResponse('')
					else:
						Bookmark.objects.create(user=request.user, 
													folder=Folder.objects.get(id=factionID), 
													bookmark = Bookmark_detail.objects.get(id=bdID)
													)
					# User_bookmark.objects
					# Bookmark_folder.objects.create(user=request.user, folder=Folder.objects.get(id=ID), bookmark = User_bookmark.objects.get(id=bID) )
					print("bookmark folder added")
					return HttpResponse('')

				elif faction =="groups":
					# bookmark = User_bookmark.objects.get(id=bID)
					if Bookmark.objects.filter(group__id= factionID,bookmark__id=bdID, isRemoved=0).exists():
						return HttpResponse('')
					else:
						Bookmark.objects.create(user=request.user, 
												group=Group.objects.get(id=factionID), 
												bookmark = Bookmark_detail.objects.get(id=bdID) 
												)
						# print("bookmark added to group")
						return HttpResponse('')
					
					

			

			elif action == 'add_folder':
				name = request.POST['name']
				did_exist = Folder.objects.filter(user_id = request.user, name = name, is_removed=0).exists()
				
				if did_exist == False:
					Folder.objects.create(user=request.user, name = name)
					folders = Folder.objects.filter(user=request.user).values()
					a = list(folders)	
				
					context = {
				    "folder_list": a,
				    "did_exist": False
					}
				else:
					context = {
				    "did_exist": True
					}
				
				return JsonResponse(context)


			elif action == 'add_group':
				name = request.POST['name']
				Group.objects.create(owner=request.user, name = name)
				# query_group = Group.objects.filter((Q(owner= request.user) | Q(member=request.user)), is_removed=0).values()
				query_group = Group.objects.select_related("member").filter((Q(owner= request.user) | Q(member=request.user)),
																			 is_removed=0).values(
																			 						"name",
																			 						"member__first_name",
																			 						"member__last_name").distinct()
				groups = list(query_group)

				context = {
			    "group_list": groups
				}
				

				return JsonResponse(context)

			elif action == 'get_folder_bookmarks':
				fID = request.POST['fID']
				queryset = Bookmark.objects.select_related("bookmark").filter(
																		folder__id=fID, user=request.user, isRemoved=0
																		).values(
																			"id", "bookmark__id", "isFavorite", "dateAccessed", "dateAdded", 
																			"isRemoved", "date_removed",
																			"bookmark__websiteTitle", "bookmark__itemType",
																			"bookmark__url", "bookmark__title", "bookmark__subtitle",
																			"bookmark__subtitle", "bookmark__author", "bookmark__description",
																			"bookmark__journalItBelongs", "bookmark__volume",
																			"bookmark__numOfCitation", "bookmark__numOfPages",
																			"bookmark__publisher", "bookmark__publicationYear",
																			"bookmark__DOI", "bookmark__ISSN", "bookmark__edition",
																			 "bookmark__numOfDownload"
																				)
				
				# cursor = connection.cursor()   
				# cursor.execute("SELECT bf.id AS bf_ID, b.* FROM User_bookmark b, Bookmark_folder bf WHERE bf.folder_id = "+ str(fID)+" AND bf.bookmark_id = b.id AND bf.user_id = "+ str(request.user.id)+" AND bf.is_removed = 0 AND b.isRemoved = 0") #| get rows of for a specific date|
				# a = dictfetchall(cursor)
				# print(a)
				a = list(queryset)
				print(len(a))
				context = {
			    "bookmarks": a
				}
				
				return JsonResponse(context)

			elif action == 'get_group_bookmarks':
				gID = request.POST['gID']
				bookmarks = Bookmark.objects.select_related("bookmark").filter(
																		group__id=gID, isRemoved=0
																		).values(
																			"id", "bookmark__id", "isFavorite", "dateAccessed", "dateAdded", 
																			"isRemoved", "date_removed",
																			"bookmark__websiteTitle", "bookmark__itemType",
																			"bookmark__url", "bookmark__title", "bookmark__subtitle",
																			"bookmark__subtitle", "bookmark__author", "bookmark__description",
																			"bookmark__journalItBelongs", "bookmark__volume",
																			"bookmark__numOfCitation", "bookmark__numOfPages",
																			"bookmark__publisher", "bookmark__publicationYear",
																			"bookmark__DOI", "bookmark__ISSN", "bookmark__edition",
																			 "bookmark__numOfDownload"
																				)
		
				# cursor = connection.cursor()   
				# cursor.execute("SELECT gf.id AS bf_ID, b.* FROM User_bookmark b, Group_bookmark gf WHERE gf.group_id = "+ str(gID)+" AND gf.bookmark_id = b.id AND gf.is_removed = 0") #| get rows of for a specific date|
				# a = dictfetchall(cursor)
				a = list(bookmarks)
				
				
				context = {
			    "bookmarks": a
				}
				
				return JsonResponse(context)

			elif action == 'remove_from_faction':
				faction_id = request.POST['faction_id']
				bookmark_id = request.POST['b_id']

				if request.POST['faction_type'] == 'folders':
	
					Bookmark.objects.filter(bookmark_id=bookmark_id,
											 user= request.user, 
											 folder__id=faction_id
											 ).update(isRemoved=1,
											 			date_removed= timezone.now()
											 			)
					
					queryset = Bookmark.objects.select_related("bookmark").filter(
																		folder__id=faction_id, user=request.user, isRemoved=0
																		).values(
																			"id", "bookmark__id", "isFavorite", "dateAccessed", "dateAdded", 
																			"isRemoved", "date_removed",
																			"bookmark__websiteTitle", "bookmark__itemType",
																			"bookmark__url", "bookmark__title", "bookmark__subtitle",
																			"bookmark__subtitle", "bookmark__author", "bookmark__description",
																			"bookmark__journalItBelongs", "bookmark__volume",
																			"bookmark__numOfCitation", "bookmark__numOfPages",
																			"bookmark__publisher", "bookmark__publicationYear",
																			"bookmark__DOI", "bookmark__ISSN", "bookmark__edition",
																			 "bookmark__numOfDownload"
																				)

					a = list(queryset)
					print(len(a))
					context = {
				    "bookmarks": a
					}
					
					return JsonResponse(context)

				if request.POST['faction_type'] == 'groups':
					print("bbokmark id: ", bookmark_id)
					print("folder id: ", faction_id)
					Bookmark.objects.filter(group__id=faction_id,
											bookmark__id=bookmark_id,
											 ).update(isRemoved=1,
											 			date_removed= timezone.now()
											 			)
					queryset = Bookmark.objects.select_related("bookmark").filter(
																		group__id=faction_id, isRemoved=0
																		).values(
																			"id", "bookmark__id", "isFavorite", "dateAccessed", "dateAdded", 
																			"isRemoved", "date_removed",
																			"bookmark__websiteTitle", "bookmark__itemType",
																			"bookmark__url", "bookmark__title", "bookmark__subtitle",
																			"bookmark__subtitle", "bookmark__author", "bookmark__description",
																			"bookmark__journalItBelongs", "bookmark__volume",
																			"bookmark__numOfCitation", "bookmark__numOfPages",
																			"bookmark__publisher", "bookmark__publicationYear",
																			"bookmark__DOI", "bookmark__ISSN", "bookmark__edition",
																			 "bookmark__numOfDownload"
																				)

					a = list(queryset)
					print(len(a))
					context = {
				    "bookmarks": a
					}
					
					return JsonResponse(context)

				# if request.POST['faction_type'] == 'trash':
				# 	# print(type(request.POST['action_type']))
				# 	if request.POST['action_type'] == '1': #if action_type is restore 

				# 		faction_id = request.POST['faction_id']
				# 		Bookmark_folder.objects.filter(id =faction_id).update(is_removed = 0, date_removed=None)
				# 		return HttpResponse('')

				# 	else:
				# 		faction_id = request.POST['faction_id']
				# 		Bookmark_folder.objects.filter(id =faction_id).update(is_removed = 2, date_removed=timezone.now)
				# 		return HttpResponse('')

			


			elif action == 'open_link':
				bID = request.POST['bID']

				Bookmark.objects.filter(bookmark__id = bID, user=request.user, group = None).update(dateAccessed = timezone.now())
				return HttpResponse('')

			elif action == 'delete_faction':
				faction_type = request.POST['faction_type']
				print('faction_type')
				if faction_type == 'folder':
					ID = request.POST['id']
					Folder.objects.filter(id = ID).update(is_removed = 1)
					print('folder deleted')
					return HttpResponse('')
				elif faction_type == 'groups':
					ID = request.POST['id']
					Group.objects.filter(id = ID).update(is_removed = 1)
					print('group deleted')
					return HttpResponse('')

			elif action == 'add_member':
				username = request.POST['id']
				gID = request.POST['gID']
				print(gID)
				
				if User_group.objects.filter(id = gID,member__username= User.objects.get(username=username)).exists():
					context={
					"result":"member"
					}
					print('member')
					return JsonResponse(context)

				elif User_group.objects.filter(id = gID,owner__username= username).exists():
					context={
					"result":"owner"
					}
					print('owner')		
					return JsonResponse(context)

				elif User.objects.filter(username=username).exists():
					User_group.objects.get(id=gID).member.add(User.objects.get(username=username))
					print("added")
					context={
					"result":"added"
					}
					return JsonResponse(context)



							

def TeraAccountSettingsView(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)
	    
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)  
			messages.success(request, 'Your password was successfully updated!' )
			return redirect('ra:tera_account_settings')
		else:

			messages.info(request, str(form.errors))
	else:

	    form = PasswordChangeForm(request.user)
	return render(request, 'accountsettings.html', {
	    'form': form})



class adminChartView(View):
	def get(self, request):
		return render(request, 'adminCharts.html')


class adminTableView(View):
	def get(self, request):
		return render(request, 'adminTables.html')

class adminRegistrationView(View):
	def get(self, request, rtype):
		# form = CreateUserForm(request.POST or None)
		# context={
		# 	"form": form
		# }
		

		return render(request, 'adminRegistration.html',{"type": rtype})#, context)
	def post(self, request, rtype):
		

		if 'btnRegister' in request.POST: 
			form = CreateUserForm(request.POST)
			if form.is_valid():
				username=request.POST['username']
				password=request.POST['password']
				first_name=request.POST['first_name']
				last_name=request.POST['last_name']
				department=request.POST['department']
				user = User(username=username,
							password = password,
							first_name = first_name,
							last_name= last_name,
							department = Department.objects.get(abbv=department)
							)
				user.save()
				messages.success(request, "User added")
				print("success", rtype)
				return redirect('ra:admin_registration_view',  rtype=rtype)
			else:
				print("error")
				return render(request, 'adminRegistration.html', {"form":form,"type": rtype})

		if request.is_ajax():
			print("nisulod asa ajax")
			if request.POST['action'] == "register_csv":
				users = json.loads(request.POST.get('users'))
				didExcept = 0
				errorRows=[]
				for row in users:
					user = User(
						username = row['username'], 
						password=make_password(row['password']),
						first_name= row['first_name'], 
						last_name=row['last_name'], 
						department =  Department.objects.get(abbv=row['department'])
						)
					try:
						user.save()
					except Exception as e:
						didExcept +=1
						errorRows.append(row)

				context ={
					"didExcept": didExcept,
					"errorRows": errorRows,
					"usersCount": len(users)
				}
				return JsonResponse(context)
		# elif 'readCSV' in request.POST:

		try:
			myfile = request.FILES['file']
			file = myfile.read().decode('utf-8')
			dict_reader = csv.DictReader(io.StringIO(file))
			users =  list(dict_reader)

			return render(request, 'adminRegistration.html', {"users":users, "type": rtype})
		except:
			messages.success(request, "please select a file first")
			return redirect('ra:admin_registration_view', rtype=rtype)




		# elif 'readCSVForm' in request.POST:

		# 	return HttpResponse('olok')

			

		# elif request.is_ajax():
		# 	action = request.POST['action']

		# 	if action =='read':
		# 		myfile = request.FILES['file']

		# 		file = myfile.read().decode('utf-8')
		# 		dict_reader = csv.DictReader(io.StringIO(file))

		# 		print(list(dict_reader))

# elif form.is_valid():
		# 	folder = request.POST.get("foldername")
		# 	form = Folders(foldername = folder)
		# 	form.save()

		# 	return redirect('ra:tera_dashboard_view')

		# elif request.method == 'POST':
		# 	if 'btnDelete' in request.POST:
		# 		print('delete button clicked')
		# 		fid = request.POST.get("folder-id")
		# 		fldr = Folders.objects.filter(id=fid).delete()
		# 		print('Recorded Deleted')
		# 		return redirect('ra:tera_dashboard_view')


class FolderViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,):

    queryset = Folder.objects.all()
    serializer_class = serializers.FolderModelSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return serializers.FolderRetrieveModelSerializer

        return super().get_serializer_class()


class UserBookmarkViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,):

    queryset = Bookmark.objects.all()
    serializer_class = serializers.UserBookmarkModelSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        serializer = serializers.UserBookmarkQuerySerializer(data=self.request.query_params)

        if not serializer.is_valid():
            return queryset.removed(False)

        removed = serializer.validated_data.get("removed")

        if removed:
            return queryset.removed()

        queryset = queryset.removed(False)


        recently_added = serializer.validated_data.get("recently_added")
        if recently_added:
            queryset = queryset.recently_added()


        recently_read = serializer.validated_data.get("recently_read")
        if recently_read:
            queryset = queryset.recently_read()


        favorite = serializer.validated_data.get("favorite")
        if favorite is not None:
            queryset = queryset.favorites(favorite)


        folder = serializer.validated_data.get("folder")
        if folder is not None:
            queryset = queryset.folder(folder)

        return queryset

    # def list(self, request, *args, **kwargs):
    # 	queryset = self.filter_queryset(self.get_queryset())

    # 	page = self.paginate_queryset(queryset)

    # 	if page is not None:
    # 		serializer = self.get_serializer(page, many=True)
    # 		return self.get_paginated_response(serializer.data)

    # 	serializer = self.get_serializer(queryset, many=True)
    # 	return Response(serializer.data)


    @action(methods=["POST"], detail=True, url_path="toggle-favorite")
    def toggle_favorite(self, *args, **kwargs):
        instance = self.get_object()

        instance.isFavorite = not instance.isFavorite
        instance.save()

        return Response(status=status.HTTP_200_OK)