from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse

class TeraIndexView(View):
	def get(self, request):

		return render(request,'1.html')

class LandingIndexView(View):
	def get(self, request):
	
		return render(request,'Login.html')

class HomePageView(View):
	def get(self, request):
	
		return render(request,'home.html')

	