from django.urls import path
from . import views

app_name = 'ra'
urlpatterns = [
	
			path('', views.TeraIndexView.as_view(), name="index_view"),
			path('/login', views.TeraLoginUser.as_view(), name='tera_login_view'),
			path('/logout', views.TeraLogout, name='logout_view'),
			path('/home',views.TeraHomepageView.as_view(), name="tera_homepage_view"),
			path('/dashboard',views.TeraDashboardView.as_view(), name="tera_dashboard_view"),
			path('/citejournal',views.TeraCreateJournalCitationView.as_view(), name="tera_citejournal_view"),
			path('/citebook',views.TeraCreateBookCitationView.as_view(), name="tera_citebook_view"),
			path('/accountsettings', views.TeraAccountSettingsView, name='tera_account_settings'),
			path('/journal-citation-result-inprint',views.JournalCitationResult.as_view(), name="journal-citation-result-inprint"),
			path('/citation_history',views.CitationHistory.as_view(), name="citation-history"),
			path('/citation_history',views.CitationDeleteView.as_view(), name="deletion_confirmation"),
			path('/search',views.TeraSearchResultsView.as_view(), name="search_result_view"),
			path('/admin', views.adminIndexView.as_view(), name="admin_index_view"),
		
			path('/practice', views.practice.as_view(), name="practice"),
			path('/practice2/search?=<sinput>&site=<site>&type=<type>', views.practice2.as_view(), name="practice2"),
			path('/practice3', views.practice3.as_view(), name="practice34"),
			
			]	