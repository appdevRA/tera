from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from .forms import CreateFolderForm
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .forms import LoginUser
from bs4 import BeautifulSoup
from .links import *
import requests
#from fake_useragent import FakeUserAgent
import ast
import json
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.http import JsonResponse
from django.db import connection
from datetime import datetime


class adminIndexView(View):
	def get(self, request):
		print('olok')

		return render(request,'adminIndex.html')

class adminChartsView(View):
	def get(self, request):
		print('olok')

		return render(request,'adminCharts.html')

class adminTablesView(View):
	def get(self, request):
		print('olok')

		return render(request,'adminTables.html')

class adminCollegesView(View):
	def get(self, request):
		print('olok')

		return render(request,'adminColleges.html')

class practice2(View):
	def get(self, request, sinput, site,type):
		print('olok')
		
		return HttpResponse(sinput +" "+site+" "+type)


		

class practice3(View):
	def get(self, request):
		print('practice3 get')
	def post(self, request):
		if request.method == 'POST' and request.is_ajax():
			print('practice 3 post')

			
			return HttpResponse(request.GET.get('search'))
		
		
		


class practice(View):
	def get(self, request):
		
		User.objects.create(username='mondejar2', password = make_password('mondejar.12345'), department=2)
		# User.objects.create(username='mondejar2', password = make_password('mondejar.12345'), department_id=2)
		cursor = connection.cursor()   
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
		# a = list(queryset)
		# context = {
		#     "bookmark_set": queryset,
		#     # "bookmark_list" : a 
		# }
		return HttpResponse('')
		# User.objects.create(username="1523-323", password="aasdqwe12345")
		# return render(request,'practice.html',context)

	def post(self, request):
		if request.method == 'POST':
			print('practice post')

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
				
				if request.session.get('proxy') == None:
					proxies = Proxies.objects.filter(isUsed = 0) # get all proxy from db
					request.session['proxy'] = testProxy(proxies,1)
					
				return redirect('ra:'+ request.session.get('previousPage'))
			else:
				return render(request,'loginInvalid.html')
		
		
					
		
		 
			
class TeraIndexView(View):
	def get(self, request):
		

		#proxies = proxy_generator2() #/ generating free proxies /
		#for proxy in proxies:  #/ saving proxies to db /
			
		#	proxy =Proxies(proxy = proxy)
		#	proxy.save()
		
		if request.session.get('proxy') == None:
			proxies = Proxies.objects.filter(isUsed = 0) # get all proxy from db
			request.session['proxy'] = testProxy(proxies,1)
		else:
			result = testProxy(request.session.get('proxy'),2) # test a single proxy

			if result == False:
				proxies = Proxies.objects.filter(isUsed = 0) # get all proxy from db
				request.session['proxy'] = testProxy(proxies,1) # test a random proxy from db
			else:
				request.session['proxy'] = result

		request.session['previousPage'] = 'index_view'
		
		context ={
			"user_id": request.user.id
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
		# header = ast.literal_eval(Headers.objects.get(id=2).text)	# converting b from string to dictionary
		# header = request.session.get('header')
		word = request.session.get('word')

		proxy = request.session.get('proxy')

		if request.session.get('website') != None:
			website = request.session.get('website')
		else:
			website = "Springeropen.com"

		if request.session.get('itemType') != None:
			itemType = request.session.get('itemType')
		else:
			itemType = "article"
						
		context = {
							'keyword': word,
							'proxy': proxy,
							'website': website,
							'itemType': itemType,
							'is_authenticated': str(request.user.is_authenticated)
		}
		
		return render(request,'searchresults.html', context)

	def post(self, request):
		
		if request.method == 'POST' and request.is_ajax():
			
			
			
			action = request.POST['action']

			if action == "search":


				if request.POST['proxy'] == None:
					proxies = Proxies.objects.filter(isUsed = 0) # get all proxy from db
					proxy = testProxy(proxies,1)


					word = request.POST['word']
					website = request.POST['site']
					itemType = request.POST['itemType']
					request.session['website'] =website
					request.session['itemType'] = itemType
					request.session['word'] = word

					a = scrape(word,proxy,itemType , website,' ', request.POST['pageNumber'])
					
					while (a == False):
						proxies = Proxies.objects.filter(isUsed = 0) # get all proxy from db
						proxy = testProxy(proxies,1)
						request.session['proxy'] = proxy
						a = scrape(request.POST['word'],proxy, itemType,website ,' ', request.POST['pageNumber'])
				


					results = a[0]	
					links = a[1]
					# print(results)
					context = {
						'results': results,
						'links': links,
						'proxy': proxy,
						'is_authenticated': request.user.is_authenticated
					}
					return JsonResponse(context)





				else:
					print("search")
					word = request.POST['word']
					request.session['word'] = word
					proxy = request.POST['proxy']
					
					website = request.POST['site']
					itemType = request.POST['itemType']
					request.session['website'] =website
					request.session['itemType'] = itemType


					a = scrape(word,proxy,itemType , website,' ', request.POST['pageNumber'])
					
					while (a == False):
						proxies = Proxies.objects.filter(isUsed = 0) # get all proxy from db
						proxy = testProxy(proxies,1)
						request.session['proxy'] = proxy
						a = scrape(request.POST['word'],proxy, itemType,website ,' ', request.POST['pageNumber'])
				


					results = a[0]	
					links = a[1]
					# print(results)
					context = {
						'results': results,
						'links': links,
						'proxy': proxy,
						'is_authenticated': request.user.is_authenticated
					}
					return JsonResponse(context)
					
			elif action == "add":
				print('bookmark button clicked')
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
					Bookmarks.objects.create(user = request.user,title = title,websiteTitle= websiteTitle,itemType= itemType,author = author, description= description, url = url, journalItBelongs= journalItBelongs, volume = volume, DOI = doi)
				elif itemType == "book":
					Bookmarks.objects.create(user = request.user,title = title,websiteTitle= websiteTitle,subtitle = subtitle, 
						itemType= itemType,author = author,numOfCitation = citation,numOfDownload= downloads,publisher=publisher, 
						description= description, url = url, edition = edition,numOfPages = pages,
						 DOI = doi)
				return HttpResponse('')
			else:
				string = bookmark.split('||')

				title = string[1].replace('\n','').replace('  ','')
				Bookmarks.objects.filter(title=title).update(isRemoved=1)
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
			


		

class TeraHomepageView(View):
	def get(self,request):
		return render(request,'home.html')	
		

class TeraDashboardView(View):
	reqCount = 0
	def get(self,request):
		print(self.reqCount)
		queryset = Bookmarks.objects.filter(user_id=request.user.id)
		request.session['previousPage'] = "tera_dashboard_view"
		a= serializers.serialize("json",queryset )

		context = {
		    "bookmark_set": queryset,
		    "bookmark_list" : a 
		}
		try:
			if request.user.id != None:
				return render(request,'collections.html', context)
			else:
				request.session['previousPage'] = 'tera_dashboard_view'
				return redirect('ra:tera_login_view')
		except:
			request.session['previousPage'] = 'tera_dashboard_view'
			return redirect('ra:tera_login_view')

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

		elif request.method == 'POST' and request.is_ajax():
				
			action = request.POST['action']

			if action == 'addFav':
				Bookmarks.objects.filter(id=request.POST['bID']).update(isFavorite=1)
				return HttpResponse('')
			elif action == 'remFav':
				Bookmarks.objects.filter(id=request.POST['bID']).update(isFavorite=0)
				return HttpResponse('')
			elif action == 'trashItem':
				Bookmarks.objects.filter(id=request.POST['bID']).update(isRemoved=1)
				return HttpResponse('')
			elif action == 'unTrashItem':
				Bookmarks.objects.filter(id=request.POST['bID']).update(isRemoved=0)
				return HttpResponse('')
			elif action == 'deleteItem':
				Bookmarks.objects.filter(id=request.POST['bID']).update(isRemoved=3)
				return HttpResponse('')


	    


class TeraCreateJournalCitationView(View):
	def get(self,request):
		return render(request,'citejournal.html')

	def post(self, request):
	 	form = CiteJournalForm(request.POST)
	 	if form.is_valid():
	 		contrib = request.POST.get("contributor")
	 		firstname = request.POST.get("fname")
	 		midnitial = request.POST.get("minitial")
	 		lastname = request.POST.get("lname")
	 		artitle = request.POST.get("ar_title")
	 		jourtitle = request.POST.get("jour_title")
	 		vol = request.POST.get("volume")
	 		iss = request.POST.get("issue")
	 		ser = request.POST.get("series")
	 		datepublished = request.POST.get("pubdate")
	 		start = request.POST.get("pagestart")
	 		end = request.POST.get("pagend")
	 		anno = request.POST.get("annotation")
	 		citeformat = request.POST.get("citationformat")
	 		reftype = request.POST.get("referencetype")
	 		form = Citations(contributor = contrib, fname = firstname, minitial = midnitial, lname = lastname, 
	 			ar_title = artitle, jour_title = jourtitle, volume = vol, issue = iss, series = ser, pubdate = datepublished, 
	 			pagestart = start, pagend = end, annotation = anno, citationformat=citeformat, referencetype = reftype)
	 		form.save()

	 		print('Data Successfully Recorded!')
	 		return redirect('ra:journal-citation-result-inprint')
	 		
	 	else:
	 		print(form.errors)
	 		return HttpResponse('Sorry, Failed to Record Data.')

class TeraCreateBookCitationView(View):
	def get(self,request):
		return render(request,'citebook.html')

class CitationDeleteView(View):
	def get(self,request):
		return render(request,'citedeleted.html')

class JournalCitationResult(View):
	def get(self, request):
		qs_journalcitation = Citations.objects.order_by('-id')

		context = {'results' : qs_journalcitation }	
		return render(request, 'citejournalresult_inprint.html', context)

class CitationHistory(View):
	def get(self, request):
		qs_journalcitation = Citations.objects.order_by('-id')

		context = {'results' : qs_journalcitation }	
		return render(request, 'citationhistory.html', context)

		if 'btnDelete' in request.POST:	
				print('delete button clicked')
				journal_id = request.POST.get("journal-id")
				journaldelete = Citations.objects.filter(id=journal_id).delete()
				print('Recorded Deleted')
		return redirect('ra:deletion_confirmation')

def TeraLogout(request):
    logout(request)
    return redirect('ra:tera_index_view')

def TeraAccountSettingsView(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            messages.success(request, 'Your password was successfully updated!' )
            return redirect('ra:tera_account_settings')
        else:
            messages.info(request, 'Incorrect Password.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accountsettings.html', {
        'form': form
    })

						