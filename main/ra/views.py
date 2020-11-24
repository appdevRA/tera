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

<<<<<<< Updated upstream
	
=======
class TeraCreateCitationView(View):
	def get(self,request):
		return render(request,'createcitation.html')

class TeraLoginView(View):
	def get(self,request):
		return render(request,'login.html')		

class TeraGrammarView(View):
	def get(self,request):
<<<<<<< Updated upstream
		return render(request,'homecopy.html')			
>>>>>>> Stashed changes
=======
		return render(request,'createcitation.html')

class TeraLoginView(View):
	def get(self,request):
		return render(request,'login.html')		

class TeraGrammarView(View):
	def get(self,request):
<<<<<<< Updated upstream
		return render(request,'homecopy.html')			
>>>>>>> Stashed changes
=======
		return render(request,'homecopy.html')			
>>>>>>> Stashed changes
