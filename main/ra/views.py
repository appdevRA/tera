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
import requests
from bs4 import BeautifulSoup
#import urllib2 
#import cookielib ## http.cookiejar in python3

class TeraIndexView(View):
	def get(self, request):

		return render(request,'landingpage.html')
		
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

		headers = {
    	'authority': 'www.sciencedirect.com',
    	'cache-control': 'max-age=0',
    	'sec-ch-ua': '^\\^',
    	'sec-ch-ua-mobile': '?0',
    	'upgrade-insecure-requests': '1',
    	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
    	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    	'sec-fetch-site': 'cross-site',
    	'sec-fetch-mode': 'navigate',
    	'sec-fetch-user': '?1',
    	'sec-fetch-dest': 'documnet',
    	'referer': 'https://id.elsevier.com/',
    	'accept-language': 'en-US,en;q=0.9',
    	'cookie': 'EUID=75fdfe63-504d-4c8a-8180-c03a43da237c; mboxes=^%^7B^%^7D; utt=2146-84ee935a77144283645aebe835a645e74f7-M0M6; mbox=session^%^2343e27bd8a91d47359facd5feee8d4048^%^231614351099^%^7CPC^%^2370b4195123dc401fa07762b437030b81.34_0^%^231677594039; fingerPrintToken=f8db7e374a427289e269fe42a5d6bc98; AMCVS_4D6368F454EC41940A4C98A6^%^40AdobeOrg=1; __cfduid=dd1b701d63bdde452e636ab8868c52a141620441918; acw=461d352a83e918411b086ee05f50f46924f0gxrqb^%^7C^%^24^%^7C9151E9CCE450711D0F498388C28EF159BAC7F3200317489478B0299961677297E0A53AEE614636E51FCAE825E31FC377B3E70131FC37F2EE0E9169905BBD791CB0469A67597464825D387A21AFA2E514; sd_access=eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..BWfY6-SuAg3zDqsDRs0f0Q.If1RR-CIK_oEWKgGCwQLg-7VqG-8rysV3WGNL02iGVF4nipgKKDii7aJbBXGjLjcsWv2LKZp0-AVmX5jITGtDh6NXPmhWR9B4kkdKNY7fS3xSWJifB7PxaxAu6diqUALpmKGfMGXeLHA0JbgbI_9Og.iFlsBlTK9WjO_1jA_73z5g; sd_session_id=1593316a7baad24fc759a6599c3ae670d69cgxrqb; id_ab=IDP; __cf_bm=8a5355bc92f6e818673baef39febbe6089acc61c-1620442903-1800-AWts+5qEQktyo0BysgEh3CbweSKz/aIaFyyThN5DUNKZg5rfB7Ky1brNV3MJCGaG76tgHFPnmeKAvA5eH7UjfIY=; has_multiple_organizations=true; AMCV_4D6368F454EC41940A4C98A6^%^40AdobeOrg=-1124106680^%^7CMCIDTS^%^7C18755^%^7CMCMID^%^7C10640528059237186110715255087884724485^%^7CMCAID^%^7CNONE^%^7CMCOPTOUT-1620450106s^%^7CNONE^%^7CMCAAMLH-1621047706^%^7C3^%^7CMCAAMB-1621047706^%^7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI^%^7CMCSYNCSOP^%^7C411-18716^%^7CvVersion^%^7C5.2.0^%^7CMCCIDH^%^7C-388222836; MIAMISESSION=a4046128-c0a2-4965-90d6-00a42c3fe273:3797895796; SD_REMOTEACCESS=eyJhY2NvdW50SWQiOiI3MzA5NCIsInRpbWVzdGFtcCI6MTYyMDQ0Mjk5NjQ4M30=; s_pers=^%^20v8^%^3D1620442997787^%^7C1715050997787^%^3B^%^20v8_s^%^3DLess^%^2520than^%^25201^%^2520day^%^7C1620444797787^%^3B^%^20c19^%^3Dsd^%^253Ahome^%^253Ahpx^%^7C1620444797792^%^3B^%^20v68^%^3D1620442996827^%^7C1620444797802^%^3B; s_sess=^%^20s_cpc^%^3D0^%^3B^%^20c21^%^3Dqs^%^253Dbreast^%^3B^%^20e13^%^3Dqs^%^253Dbreast^%^253A1^%^3B^%^20c13^%^3Drelevance-desc^%^3B^%^20s_sq^%^3D^%^3B^%^20s_ppvl^%^3Dsd^%^25253Ahome^%^25253Ahpx^%^252C22^%^252C22^%^252C969^%^252C1365^%^252C969^%^252C1920^%^252C1080^%^252C1^%^252CP^%^3B^%^20e41^%^3D1^%^3B^%^20s_cc^%^3Dtrue^%^3B^%^20s_ppv^%^3Dsd^%^25253Ahome^%^25253Ahpx^%^252C22^%^252C21^%^252C969^%^252C1365^%^252C969^%^252C1920^%^252C1080^%^252C1^%^252CP^%^3B',
		}
		response = requests.get('https://www.sciencedirect.com/search?qs=war', headers=headers)
		soup = BeautifulSoup(response.content, "html.parser")
		print(soup.prettify)
		return redirect('https://www.sciencedirect.com/search?qs=war')	

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

						