from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse

class TeraIndexView(View):
	def get(self, request):

		return render(request,'landingpage.html')

class TeraSearchResultsView(View):
	def get(self,request):
		return render(request,'3.html')	

class TeraHomepageView(View):
	def get(self,request):
		return render(request,'home.html')	

class TeraDashboardView(View):
	def get(self,request):
		return render(request,'dashboard.html')

class TeraCreateCitationView(View):
	def get(self,request):
		return render(request,'createcitation.html')		
						