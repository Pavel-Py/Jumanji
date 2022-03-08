from django.contrib import admin
from django.urls import path, re_path

from jum.views import MainView, CompanyView, AllVacanciesView, VacanciesByCatView, VacancyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='index'),
    re_path(r'^vacancy/(?P<pk>\d+)', VacancyView.as_view(), name='vacancy'),
    re_path(r'company/(?P<pk>\d+)', CompanyView.as_view(), name='company'),
    path('vacancies/', AllVacanciesView.as_view(), name='allvacancies'),
    path('vacancies/cat/<str:field>', VacanciesByCatView.as_view(), name='catvacancies'),
]




    # path('vacancies/', VacaciesView.as_view()),
    # path('vacancies/cat/<str:field>', VacaciesView.as_view()),
    # path('companies/<int:company_id>', CompanyView.as_view()),
    # path('vacancies/<int:vacancy_id>', VacancyView.as_view()),
