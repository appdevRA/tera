from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.utils import timezone
from .forms import CreateFolderForm
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

from .forms import LoginUser

from bs4 import BeautifulSoup
from .links import *
import requests
from django.core import serializers
#from fake_useragent import FakeUserAgent

class practice(View):
	def get(self, request):
		
		a = ['a','b']
		context={
			'number':a,
			'user_id': request.session.get('id')
		}
		return render(request,'practice.html',context)

	def post(self, request):
		if request.method == 'POST' and request.is_ajax():
			
			link = request.POST['link']
			
			# if len(link) > 1:
			# 	counter = request.POST['counter']
			#if len(link) <2:
			# print(counter)
			# print(link.keys())
			# Bookmarks.objects.create(user = User.objects.get(id=request.session.get('id')),link = link)
			
			print(link)
			# link = request.POST['link']

			
			return render(request,'login.html')	
		
		


class TeraLoginUser(View): 

	def get(self,request):
		
		# proxies = proxy_generator2() #/ generating free proxies /
		# for proxy in proxies:  #/ saving proxies to db /
			
		# 	proxy = Proxies(proxy = proxy)
		# 	proxy.save()

		if( request.session.get('id') != None):
			return redirect("ra:index_view")
		else:
			return render(request,'login.html')	


		
		

	def post(self, request):
		
		if request.method == 'POST':
			
			
			uname = request.POST.get('username')
			passw = request.POST.get('password')
			try:
				user = User.objects.get(username = uname, password = passw)
				request.session['id'] = user.id
				
				return redirect("ra:index_view")
			except:
				return HttpResponse("Invalid username or password. ")
					
		
		    # 
		# else:
			
class TeraIndexView(View):
	def get(self, request):
		

		#proxies = proxy_generator2() #/ generating free proxies /
		#for proxy in proxies:  #/ saving proxies to db /
			
		#	proxy =Proxies(proxy = proxy)
		#	proxy.save()
		
		#user = User.objects.get(username = 'tt', password = 'tt')
		
		proxies = Proxies.objects.filter(isUsed = 0) # get all proxy from db
		a = testProxy(proxies).proxy
		
		User.objects.filter(id = request.session['id']).update(proxy = a) # set proxy to user
		
		#request.session['proxy'] = a
		#request.session['id'] = 1
		
		
		#scienceDirect(testProxy(proxies))
		#scirp('engineer', practice(testProxy(proxies)), 'a')
		#practice()
		#springer('war', testProxy(proxies))
		#print(proxyID.id)
		#x = Proxies.objects.filter(id = proxyID.id).update(isUsed = 1)
		return render(request,'landingpage.html')

	def post(self, request):
		if request.method == 'POST':
			request.session['word'] = request.POST.get("keyword")
			return redirect('ra:search_result_view')
		


class TeraSearchResultsView(View):
	

	def get(self,request):
		

		proxies = Proxies.objects.filter(isUsed = 0)
		word = request.session.get('word')
		refType = 'springer article'
		

		a = scrape(word,request.session.get('proxy') , 'article',1, 'springer open')
		# a = springer(word,request.session.get('proxy') , 'article',1)
		while (a == False):

			proxy = testProxy(proxies).proxy
			request.session['proxy'] = proxy
			a = scrape(word,request.session.get('proxy') , 'article',1, 'springer open')
		
		results = a[0]	
		links = a[1]				
		context = {
							'keyword': word,
							'results': results,
							'links': links,
							'type': refType,
							'id': request.session.get('id')
		}

		return render(request,'searchresults.html', context)

	def post(self, request):

		proxies = Proxies.objects.filter(isUsed = 0)

		if 'btnSearchbar' in request.POST:
			word = request.POST.get("searchbar")
			refType = 'springer article'
			
			a = scrape(word, request.session.get('proxy') , 'article', 1, 'springer open')

			while (a == False):
				proxy = testProxy(proxies).proxy
				request.session['proxy'] = proxy
				a = scrape(word, request.session.get('proxy') , 'article', 1, 'springer open')


			springers = a[0]	
			springLinks = a[1]		
			context = {
					'keyword': word,
					'results': springers,
					'links': springLinks,
					'type': refType
			}
	
			return render(request,'searchresults.html', context)

		elif 'btnArticles' in request.POST:
			refType = 'scirp article'
			word = request.POST.get("search")

			a = scrape(word, request.session.get('proxy') , 'article', 1, 'scirp')
			
			while (a == False):
				proxy = testProxy(proxies).proxy
				request.session['proxy'] = proxy
				a = scrape(word, request.session.get('proxy') , 'article', 1, 'scirp')
			
			scienceDirects = a[0]
			scienceLinks = a[1]

			springers = a[0]	
			springLinks = a[1]	

			context = {
					'keyword': word,
					'results': springers,
					'links': springLinks,
					'type': refType
			}

			return render(request,'searchresults.html', context)

		elif 'btnJournal' in request.POST:
			word = request.POST.get("search")
			refType = 'scienceDirectJournal'
			
			a = scrape(word,request.session.get('proxy') , 'journal',1, 'science direct')


			while (a == False):
				proxy = testProxy(proxies).proxy
				request.session['proxy'] = proxy
				a = scrape(word,request.session.get('proxy') , 'journal',1, 'science direct')

			scienceDirects = a[0]
			scienceLinks = a[1]
				
			context = {
				'keyword': word,
					'results': scienceDirects,
					'links': scienceLinks,
					'type': refType
					
			}

			return render(request,'searchresults.html', context)

		elif 'btnBook' in request.POST:
			word = request.POST.get("search")
			refType = 'tandfon article'

			a = scrape(word,request.session.get('proxy') , 'article',1, 'tandfonline')


			while (a == False):
				proxy = testProxy(proxies).proxy
				request.session['proxy'] = proxy
				a = scrape(word,request.session.get('proxy') , 'article',1, 'tandfonline')
			
			scienceDirects = a[0]
			scienceLinks = a[1]

			
				
			context = {
					'keyword': word,
					'results': scienceDirects,
					'links': scienceLinks,
					'type': refType
					
			}

			return render(request,'searchresults.html', context)


		elif request.method == 'POST' and request.is_ajax():
			
			bookmark = request.POST['link']
			
			string = bookmark.split('||')
			site = string[0]
			title = string[1].replace('\n','').replace('  ','')
			link = string[2]
			print(bookmark)
			print(site, title, link)
			

			
			Bookmarks.objects.create(user = User.objects.get(id=request.session.get('id')), siteName=site, title=title, link = link)
			
			
			return HttpResponse('')


class TeraHomepageView(View):
	def get(self,request):
		return render(request,'home.html')	
		

class TeraDashboardView(View):
	def get(self,request):
		userbookmarks = Bookmarks.objects.filter(user_id= request.session.get('id'))
		
			
		context = { 'bookmarks': userbookmarks}
		return render(request,'collections.html', context)

	def post(self, request):
	 	form = CreateFolderForm(request.POST)
	 	if form.is_valid():
	 		folder = request.POST.get("foldername")
	 		form = Folders(foldername = folder)
	 		form.save()

	 		return redirect('ra:tera_dashboard_view')

	 	if request.method == 'POST':
	 		if 'btnDelete' in request.POST:
	 			print('delete button clicked')
	 			fid = request.POST.get("folder-id")
	 			fldr = Folders.objects.filter(id=fid).delete()
	 			print('Recorded Deleted')
	 		return redirect('ra:tera_dashboard_view')		

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

						