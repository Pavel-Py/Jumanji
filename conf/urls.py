from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, re_path

from jum.views import MainView, CompanyView, AllVacanciesView, VacanciesByCatView, VacancyView, LoginUserView, \
    CompanyEditView, CompanyCreateView, CompanyStartView, UserVacancyView, VacancyCreteView, \
    VacancyEditView, ApplicationsView, UserCompanyView
from jum.views import custom_handler500, custom_handler404, RegisterUserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='index'),
    re_path(r'^vacancies/$', AllVacanciesView.as_view(), name='all_vacancies'),
    re_path(r'^vacancy/(?P<pk>\d+)/$', VacancyView.as_view(), name='vacancy'),
    re_path(r'^company/(?P<pk>\d+)/$', CompanyView.as_view(), name='company'),
    re_path(r'vacancies/cat/(?P<slug>\w+)/$', VacanciesByCatView.as_view(), name='cat_vacancies'),
    re_path(r'^login/$', LoginUserView.as_view(), name='login'),
    re_path(r'^register/$', RegisterUserView.as_view(), name='register'),
    re_path(r'^logout/$', LogoutView.as_view(), name='logout'),
    re_path(r'^user-company/$', UserCompanyView.as_view(), name='user-company'),
    re_path(r'^company-edit/$', CompanyEditView.as_view(), name='company-edit'),
    re_path(r'^company-create/$', CompanyCreateView.as_view(), name='company-create'),
    re_path(r'^company-start/$', CompanyStartView.as_view(), name='company-start'),
    re_path(r'^user-vacancy/$', UserVacancyView.as_view(), name='user-vacancy'),
    re_path(r'^vacancy-create/$', VacancyCreteView.as_view(), name='vacancy-create'),
    re_path(r'^vacancy-edit/(?P<pk>\d+)/$', VacancyEditView.as_view(), name='vacancy-edit'),
    re_path(r'^applications/(?P<pk>\d+)/$', ApplicationsView.as_view(), name='applications')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = custom_handler404
handler500 = custom_handler500
