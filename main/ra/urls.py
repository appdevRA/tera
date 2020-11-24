from django.urls import path
from . import views

app_name = 'ra'
urlpatterns = [
	
			path('index', views.TeraIndexView.as_view(), name="tera_index_view"),
			path('landing', views.LandingIndexView.as_view(), name="landing_index_view"),
    		path('homepage', views.HomePageView.as_view(), name="home_page_view"),

]