from django.urls import path
from . import views

app_name = 'ra'
urlpatterns = [
	
			path('index', views.TeraIndexView.as_view(), name="tera_index_view"),
			path('results',views.TeraSearchResultsView.as_view(), name="tera_search_results_view")
			

]