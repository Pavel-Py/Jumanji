from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound, HttpResponseServerError, Http404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.base import TemplateView, RedirectView

from jum.forms import RegisterUserForm, LoginUserForm, CompanyCreate, VacancyCreate, ApplicationCreate
from jum.models import Specialty, Vacancy, Company, Application


class MainView(TemplateView):
    template_name = 'jum/index.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        specialities_amount = {}
        for spec in Specialty.objects.all():
            specialities_amount[spec] = spec.vacancies.count()
        context['specialities_amount'] = specialities_amount
        company_amount = {}
        for comp in Company.objects.all():
            company_amount[comp] = comp.vacancies.count()
        context['company_amount'] = company_amount
        return context


class CompanyView(DetailView):
    model = Company
    template_name = 'jum/company.html'

    def get_context_data(self, **kwargs):
        context = super(CompanyView, self).get_context_data(**kwargs)
        context['vacancies'] = Vacancy.objects.filter(company__pk=self.kwargs['pk'])
        return context


class VacanciesByCatView(ListView):
    model = Vacancy
    template_name = 'jum/vacancies.html'

    def get_queryset(self):
        return Vacancy.objects.filter(specialty__code=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(VacanciesByCatView, self).get_context_data(**kwargs)
        context['specialty'] = Specialty.objects.get(code=self.kwargs['slug'])
        return context


class AllVacanciesView(ListView):
    model = Vacancy
    template_name = 'jum/vacancies.html'
    context_object_name = 'vacancies'


class VacancyView(CreateView):
    model = Application
    template_name = 'jum/vacancy.html'
    form_class = ApplicationCreate

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.vacancy = Vacancy.objects.get(id=self.kwargs['pk'])
        form.save()
        return redirect('all_vacancies')

    def get_context_data(self, **kwargs):
        context = super(VacancyView, self).get_context_data(**kwargs)
        context['vacancy'] = Vacancy.objects.get(id=self.kwargs['pk'])
        return context


class RegisterUserView(CreateView):
    model = User
    form_class = RegisterUserForm
    template_name = 'jum/register.html'
    success_url = reverse_lazy('login')


class LoginUserView(LoginView):
    model = User
    form_class = LoginUserForm
    template_name = 'jum/login.html'


class UserCompanyView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if Company.objects.filter(owner=self.request.user.id).count() > 0:
            return '/company-edit/'
        else:
            return '/company-start/'


class CompanyStartView(TemplateView):
    template_name = 'jum/company-start.html'


class CompanyCreateView(CreateView):
    model = Company
    form_class = CompanyCreate
    template_name = 'jum/company-create.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.save()
        return redirect('company-edit')


class CompanyEditView(UpdateView):
    model = Company
    template_name = 'jum/company-edit.html'
    form_class = CompanyCreate
    success_url = reverse_lazy('company-edit')

    def get_object(self, queryset=None):
        return Company.objects.get(owner=self.request.user.id)


class UserVacancyView(ListView):
    model = Vacancy
    template_name = 'jum/user-vacancy.html'

    def get_queryset(self):
        user_company = Company.objects.get(owner=1).id
        return Vacancy.objects.filter(company=user_company)


class VacancyCreteView(CreateView):
    model = Vacancy
    template_name = 'jum/vacancy-create.html'
    form_class = VacancyCreate

    def form_valid(self, form):
        form.instance.company = Company.objects.get(owner=self.request.user.id)
        form.save()
        return redirect('company-edit')


class VacancyEditView(UpdateView):
    model = Vacancy
    template_name = 'jum/vacancy-edit.html'
    form_class = VacancyCreate
    success_url = 'user-vacancy'

    def get_object(self, queryset=None):
        user_company = Company.objects.get(owner=self.request.user.id)
        vacancy = Vacancy.objects.get(id=self.kwargs['pk'])
        if user_company == vacancy.company:
            return Vacancy.objects.get(id=self.kwargs['pk'])
        else:
            raise Http404()


class ApplicationsView(ListView):
    model = Application
    template_name = 'jum/applications.html'

    def get_queryset(self):
        return Application.objects.filter(vacancy_id=self.kwargs['pk'])


def custom_handler404(request, exception):
    return HttpResponseNotFound('Страница не найдена, ошибка 404')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')
