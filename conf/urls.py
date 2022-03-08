from django.contrib import admin
from django.urls import path, re_path

from jum.views import MainView, CompanyView, AllVacanciesView, VacanciesByCatView, VacancyView, custom_handler404, \
    custom_handler500

handler404 = custom_handler404
handler500 = custom_handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='index'),
    path('vacancies/', AllVacanciesView.as_view(), name='allvacancies'),
    re_path(r'^vacancy/(?P<pk>\d+$)', VacancyView.as_view(), name='vacancy'),
    re_path(r'company/(?P<pk>\d+$)', CompanyView.as_view(), name='company'),
    re_path(r'vacancies/cat/(?P<field>\w+$)', VacanciesByCatView.as_view(), name='catvacancies'),
]