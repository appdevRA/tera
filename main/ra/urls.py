from django.urls import path
from . import views

app_name = 'ra'
urlpatterns = [
	
			path('index', views.TeraIndexView.as_view(), name="tera_index_view"),
<<<<<<< Updated upstream
			path('landing', views.LandingIndexView.as_view(), name="landing_index_view"),
    		path('homepage', views.HomePageView.as_view(), name="home_page_view"),

=======
			path('home',views.TeraHomepageView.as_view(), name="tera_homepage_view"),
			path('dashboard',views.TeraDashboardView.as_view(), name="tera_dashboard_view"),
			path('create_citation',views.TeraCreateCitationView.as_view(), name="tera_createcitation_view"),
			path('login',views.TeraLoginView.as_view(), name="tera_login_view"),
			path('grammar',views.TeraGrammarView.as_view(), name="tera_grammar_view"),
			
>>>>>>> Stashed changes
]