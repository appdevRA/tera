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
from django.core import serializers
from django.contrib.auth.hashers import make_password


class practice(View):
	def get(self, request):
		queryset = Bookmarks.objects.filter(user_id=1)
		
		
		
		# marker_list = []
		a= serializers.serialize("json",queryset )
		# for instance in queryset:
		# 	b_id = int(instance.id)
		# 	title = str(instance.title)
		# 	url = str(instance.url)
		# 	marker_list += [[b_id, title, url]]

		context = {
		    # "queryset": json.dumps(queryset),
		    # "queryset1": json.dumps(marker_list)
		    "bookmark_set": queryset,
		    "bookmark_list" : a 
		}
		# User.objects.create(username="1523-323", password="aasdqwe12345")
		return render(request,'login.html',context)

	def post(self, request):
		if request.method == 'POST' and request.is_ajax():
			
			link = request.POST['link']
			header = request.POST['header']
			
			Headers.objects.create(text = header)
			
			print(link)
			# link = request.POST['link']

			
			return render(request,'login.html')	
		
		


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
			request.session['previousPage'] = 'index_view'
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
			request.session['previousPage'] ='index_view'
			return redirect('ra:search_result_view')
		


class TeraSearchResultsView(View):
	

	def get(self,request):
		# header = ast.literal_eval(Headers.objects.get(id=2).text)	# converting b from string to dictionary
		# header = request.session.get('header')
		word = request.session.get('word')
		proxy = request.session.get('proxy')
		request.session['previousPage'] = 'search_result_view'
		
		
	
		refType = 'Springeropen.com Article'
		
		a = scrape(word,proxy , 'article',1, 'Springeropen.com', ' ')
		
		while (a == False):
			proxies = Proxies.objects.filter(isUsed = 0) # get all proxy from db
			proxy = testProxy(proxies,1)
			request.session['proxy'] = proxy
			a = scrape(word,proxy , 'article',1, 'Springeropen.com', ' ')
		
		results = a[0]	
		links = a[1]				
		context = {
							'keyword': word,
							'results': results,
							'links': links,
							'type': refType,
							'user_id': request.user.is_authenticated
		}
		return render(request,'searchresults.html', context)

	def post(self, request):
		header = request.session.get('header')
		proxy = request.session.get('proxy')
		#header = ast.literal_eval(Headers.objects.get(id=2).text)	# converting b from string to dictionary

		if 'btnSearchbar' in request.POST:
			word = request.POST.get("searchbar")
			request.session['word'] = word
			
			
			refType = 'Springeropen.com Article'
			a = scrape(word, proxy , 'article', 1, 'Springeropen.com', header)

			while (a == False):
				proxies = Proxies.objects.filter(isUsed = 0) # get all proxy from db
				proxy = testProxy(proxies,1)
				request.session['proxy'] = proxy
				a = scrape(word, proxy , 'article', 1, 'Springeropen.com', header)


			springers = a[0]	
			springLinks = a[1]		
			context = {
					'keyword': word,
					'results': springers,
					'links': springLinks,
					'type': refType,
					'user_id': request.user.is_authenticated
			}
	
			return render(request,'searchresults.html', context)

		elif 'btnArticles' in request.POST:
			
			word = request.POST.get("search")
			request.session['word'] = word

			refType = 'Scirp.org Article'
			a = scrape(word, proxy , 'article', 1, 'Scirp.org', header)
			
			while (a == False):
				proxies = Proxies.objects.filter(isUsed = 0) # get all proxy from db
				proxy = testProxy(proxies,1)
				a = scrape(word, proxy , 'article', 1, 'Scirp.org', header)
			
			scienceDirects = a[0]
			scienceLinks = a[1]

			springers = a[0]	
			springLinks = a[1]	

			context = {
					'keyword': word,
					'results': springers,
					'links': springLinks,
					'type': refType,
					'user_id': request.user.is_authenticated
			}

			return render(request,'searchresults.html', context)

		elif 'btnJournal' in request.POST:
			word = request.POST.get("search")
			request.session['word'] = word
			refType = 'Sciencedirect.com Article'

			
			a = scrape(word,proxy , 'journal',1, 'Sciencedirect.com', header)


			while (a == False):
				proxies = Proxies.objects.filter(isUsed = 0) # get all proxy from db
				proxy = testProxy(proxies,1)
				a = scrape(word,proxy , 'journal',1, 'Sciencedirect.com', header)

			scienceDirects = a[0]
			scienceLinks = a[1]
				
			context = {
					'keyword': word,
					'results': scienceDirects,
					'links': scienceLinks,
					'type': refType,
					'user_id': request.user.is_authenticated
			}

			return render(request,'searchresults.html', context)

		elif 'btnBook' in request.POST:
			word = request.POST.get("search")
			
			request.session['word'] = word
			refType = 'Springeropen.com Book'
			a = scrape(word,proxy , 'book',1, 'Springeropen.com', header)


			while (a == False):
				proxy = testProxy(proxies).proxy
				request.session['proxy'] = proxy
				a = scrape(word,proxy , 'book',1, 'Springeropen.com', header)
			
			scienceDirects = a[0]
			scienceLinks = a[1]

			
				
			context = {
					'keyword': word,
					'results': scienceDirects,
					'links': scienceLinks,
					'type': refType,
					'user_id': request.user.is_authenticated
					
			}

			return render(request,'searchresults.html', context)


		elif request.method == 'POST' and request.is_ajax():
			print('bookmark button clicked')
			bookmark = request.POST['bookmark']
			action = request.POST['action']
			if action == "add":
				string = bookmark.split('||')
				refType = string[0]

				title = string[1].replace('\n','').replace('  ','')
				url = string[2]
				# print(bookmark)
				
				detail = details(url, request.session.get('proxy'),refType)

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
				if itemType == "Article":
					Bookmarks.objects.create(user = request.user,title = title,websiteTitle= websiteTitle,itemType= itemType,author = author, description= description, url = url, journalItBelongs= journalItBelongs, volume = volume, DOI = doi)
				elif itemType == "Book":
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
	def get(self,request):
		queryset = Bookmarks.objects.filter(user_id=request.user.id)

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
			try:
				deleteID = request.POST['deleteID']
			# print(deleteID)
				Bookmarks.objects.filter(id=deleteID).update(isRemoved=1)
				return HttpResponse('')
			except:
				favoriteID = request.POST['favoriteID']
			
				Bookmarks.objects.filter(id=favoriteID).update(isFavorite=1)
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
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            messages.success(request, 'Your password was successfully updated!')
            return redirect('ra:tera_account_settings')
        else:
            messages.info(request, 'Password cannot be changed.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accountsettings.html', {
        'form': form
    })

						