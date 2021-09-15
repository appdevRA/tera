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
from .forms import CreateUserForm
import bs4
from bs4 import BeautifulSoup
from .links import *
import requests
from django.core import serializers
#from fake_useragent import FakeUserAgent


class TeraIndexView(View):
	def get(self, request):
		

		#proxies = proxy_generator() #/ generating free proxies /
		#for proxy in proxies:  #/ saving proxies to db /
			
		#	proxy =Proxies(proxy = proxy)
		#	proxy.save()
		
		#user = User.objects.get(username = 'tt', password = 'tt')
		
		proxies = Proxies.objects.filter(isUsed = 0) # get all proxy from db
		a = testProxy(proxies, 1).proxy
		
		#User.objects.filter(id = 1).update(proxy = a) # set proxy to user
		
		request.session['proxy'] = a
		request.session['id'] = 1
		#practice('book')
		
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
		refType = 'tandFonJournal'
		proxy = request.session.get('proxy')
		a = tandFOnline(word, proxy , 'article')

		while (a == False):

			proxy = testProxy(proxies, 1).proxy
			request.session['proxy'] = proxy
			a = tandFOnline(word, proxy , 'article')
		
		results = a[0]	
		links = a[1]				
		context = {
							'keyword': word,
							'results': results,
							'links': links,
							'type': refType
		}

		return render(request,'searchresults.html', context)

	def post(self, request):

		proxies = Proxies.objects.filter(isUsed = 0)

		if 'btnSearchbar' in request.POST:
			word = request.POST.get("searchbar")
			refType = 'tandFon'
			proxy = request.session.get('proxy')

			a = tandFOnline(word, proxy , 'journal')

			while (a == False):
				proxy = testProxy(proxies, 1).proxy
				request.session['proxy'] = proxy
				a = tandFOnline(word, proxy , 'journal')


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
			refType = 'springerArticle'
			word = request.POST.get("search")

			a = springer(word,request.session.get('proxy'), 'article')
			
			while (a == False):
				proxy = testProxy(proxies, 1).proxy
				request.session['proxy'] = proxy
				a = springer(word, proxy , 'article')
			
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
			
			a = scienceDirect(word, request.session.get('proxy'), 'journal')


			while (a == False):
				proxy = testProxy(proxies, 1).proxy
				request.session['proxy'] = proxy
				a = scienceDirect(word, proxy , 'journal')

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
			refType = 'scripArticle'

			a = scirp(word, request.session.get('proxy'), 'article')


			while (a == False):
				proxy = testProxy(proxies, 1).proxy
				request.session['proxy'] = proxy
				a = scirp(word, proxy , 'article')
			
			scienceDirects = a[0]
			scienceLinks = a[1]

			
				
			context = {
					'keyword': word,
					'results': scienceDirects,
					'links': scienceLinks,
					'type': refType
					
			}

			return render(request,'searchresults.html', context)
		

class TeraLoginUser(View): 

	def get(self,request):
		
		print(request.session.get('id'))	
		return redirect('ra:tera_homepage_view')

class TeraHomepageView(View):
	def get(self,request):
		return render(request,'home.html')	
		

class TeraDashboardView(View):
	def get(self,request):
		qs_folders = Folders.objects.all()
		print (qs_folders)
			
		context = { 'folders': qs_folders}
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

						