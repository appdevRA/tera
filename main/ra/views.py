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
from selenium import webdriver
import os


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
		
		

		cookies = {
		    'JSESSIONID': 'df0a6622ceac0af8',
		}

		headers = {
		    'Connection': 'keep-alive',
		    'sec-ch-ua': '^\\^',
		    'sec-ch-ua-mobile': '?0',
		    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56',
		    'content-type': 'text/plain',
		    'Accept': '*/*',
		    'Origin': 'https://www.sciencedirect.com',
		    'Sec-Fetch-Site': 'cross-site',
		    'Sec-Fetch-Mode': 'cors',
		    'Sec-Fetch-Dest': 'empty',
		    'Referer': 'https://www.sciencedirect.com/',
		    'Accept-Language': 'en-US,en;q=0.9',
		}

		params = (
		    ('a', '884506234'),
		    ('sa', '1'),
		    ('v', '1169.7b094c0'),
		    ('t', 'Unnamed^%^20Transaction'),
		    ('rst', '41883'),
		    ('ck', '1'),
		    ('ref', 'https://www.sciencedirect.com/search?qs=computer'),
		)

		data = 'bel.6;e,\'fi,iki,2;5,\'type,\'pointerdown;6,\'fid,1.;e,\'lcp,20b,2;6,\'size,16950.;5,\'eid'

		response = requests.post('https://bam.nr-data.net/events/1/7ac4127487', headers=headers, params=params, cookies=cookies, data=data)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('https://bam.nr-data.net/events/1/7ac4127487?a=884506234&sa=1&v=1169.7b094c0&t=Unnamed^%^20Transaction&rst=41883&ck=1&ref=https://www.sciencedirect.com/search', headers=headers, cookies=cookies, data=data)


		#scirp = requests.get("https://www.scirp.org/journal/Articles.aspx?searchCode="+word)
		sciencedirect = requests.get("https://www.sciencedirect.com/", headers=headers, params=params, cookies=cookies, data=data)
		#scirper = requests.get("https://www.springeropen.com/search?query="+word)
		soup = BeautifulSoup(sciencedirect.content, "html.parser")

		#print(soup)
		#row = soup.find_all('ul')
		#print(results)
		#for p in row:
		#	sp = p.find('span')
		#	if sp!= None:

		#		titles.append(sp.find('a').text)


		t = soup.find_all('a',  'data-test:title-link')
		print(soup)
			#a = span.find('a')
			
			#titles.append(title.find_all('p'))
			
		
		#print(titles[0])

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
		user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"

		self.options = webdriver.ChromeOptions()
		self.options.headless = True
		self.options.add_argument(f'user-agent={user_agent}')
		self.options.add_argument("--window-size=1920,1080")
		self.options.add_argument('--ignore-certificate-errors')
		self.options.add_argument('--allow-running-insecure-content')
		self.options.add_argument("--disable-extensions")
		self.options.add_argument("--proxy-server='direct://'")
		self.options.add_argument("--proxy-bypass-list=*")
		self.options.add_argument("--start-maximized")
		self.options.add_argument('--disable-gpu')
		self.options.add_argument('--disable-dev-shm-usage')
		self.options.add_argument('--no-sandbox')
		self.driver = webdriver.Chrome(executable_path="chromedriver.exe", options=self.options)
		
		self.driver.get("google.com")
		self.driver.get_screenshot_as_file("s.png")
		
		return redirect('https://www.sciencedirect.com/search?qs=computer')	
		#return redirect('https://www.scirp.org/journal/Articles.aspx?searchCode=computer')	

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

						