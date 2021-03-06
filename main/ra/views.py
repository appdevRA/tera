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
from bs4 import BeautifulSoup
import requests
#import urllib2 
#import cookielib ## http.cookiejar in python3

class TeraIndexView(View):
	def get(self, request):

		return render(request,'la1ndingpage.html')
		
def TeraLoginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            login(request, user)
            return redirect('ra:tera_homepage_view')
        else:
            messages.info(request, '*Incorrect username or password')
    
    context = {}
    return render(request,'login.html',context)


class TeraSearchResultsView(View):
	def get(self,request):
		return render(request,'3.html')	

class TeraHomepageView(View):
	def get(self,request):
		word = 'computer'
		titles = []
		links = []
		span = []
		
		
		page = requests.get("https://www.scirp.org/journal/Articles.aspx?searchCode="+word)
		soup = BeautifulSoup(page.content, "html.parser")
		
		row = soup.find_all('ul')
		#print(results)
		for p in row:
			sp = p.find('span')
			if sp!= None:

				titles.append(sp.find('a').text)

		print(titles[1],"\n", titles[2])
			#a = span.find('a')
			
			#titles.append(title.find_all('p'))
			
		
		

		#for result in r2:
		#	print(result.text)
		#titles
		#soupTitles = soup.find_all('li', class_='publication branded u-padding-xs-ver js-publication')
		#print(soupTitles)
		#for n in soupTitles:
		#	print(n.text)
			#titles.append(n.text)
		
		#links
		#rLink = soup.find_all('li', class_='publication branded u-padding-xs-ver js-publication')
		#for n in rLink:
		#	links.append(n.find('a')['href'])
			#print(links)
		#a = requests.get("https://www.sciencedirect.com" +links[0],headers=jHeaders)

		#soup = BeautifulSoup(a.content, "html.parser")
		
		
		
		
		return redirect('https://www.scirp.org/journal/Articles.aspx?searchCode=computer')	

class TeraDashboardView(View):
	def get(self,request):
		qs_folders = Folders.objects.all()
		print (qs_folders)
			
		context = { 'folders': qs_folders}
		return render(request,'dashboard.html', context)

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

						