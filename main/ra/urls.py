from django.urls import path
from . import views

app_name = 'ra'
urlpatterns = [
	
			path('index', views.TeraIndexView.as_view(), name="tera_index_view"),
			

]