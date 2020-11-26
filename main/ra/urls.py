from django.urls import path
from . import views

app_name = 'ra'
urlpatterns = [
	
			path('index', views.TeraIndexView.as_view(), name="tera_index_view"),
			path('home',views.TeraHomepageView.as_view(), name="tera_homepage_view"),
			path('dashboard',views.TeraDashboardView.as_view(), name="tera_dashboard_view"),
			path('createcitation',views.TeraCreateCitationView.as_view(), name="tera_createcitation_view"),
			
]