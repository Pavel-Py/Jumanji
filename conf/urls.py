from django.contrib import admin
from django.urls import path, re_path

from jum.views import MainView, CompanyView, AllVacanciesView, VacanciesByCatView, VacancyView
from jum.views import custom_handler500, custom_handler404

handler404 = custom_handler404
handler500 = custom_handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='index'),
    re_path(r'^vacancies/$', AllVacanciesView.as_view(), name='all_vacancies'),
    re_path(r'^vacancy/(?P<pk>\d+)/$', VacancyView.as_view(), name='vacancy'),
    re_path(r'^company/(?P<pk>\d+)/$', CompanyView.as_view(), name='company'),
    re_path(r'vacancies/cat/(?P<field>\w+)/$', VacanciesByCatView.as_view(), name='cat_vacancies'),
]
