from django.urls import path
from . import views

app_name = 'ra'
urlpatterns = [
	
			path('', views.TeraIndexView.as_view(), name="index_view"),
			path('/login', views.TeraLoginUser.as_view(), name='tera_login_view'),
			path('/dashboard',views.TeraDashboardView.as_view(), name="tera_dashboard_view"),
			path('/accountsettings', views.TeraAccountSettingsView, name='tera_account_settings'),
			path('/search',views.TeraSearchResultsView.as_view(), name="search_result_view"),
			path('/admin', views.adminIndexView.as_view(), name="admin_index_view"),
			path('/admin/charts', views.adminChartView.as_view(), name="admin_chart_view"),
			path('/admin/table', views.adminTableView.as_view(), name="admin_table_view"),
			path('/practice', views.practice.as_view(), name="practice"),
			path('/practice2/search?=<sinput>&site=<site>&type=<type>', views.practice2.as_view(), name="practice2"),
			path('/practice3', views.practice3.as_view(), name="practice34"),
			
			]	