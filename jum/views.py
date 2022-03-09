from django.http import HttpResponseNotFound, HttpResponseServerError
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView

from jum.models import Specialty, Vacancy, Company


class MainView(TemplateView):
    template_name = 'jum/index.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        specialities_amount = {}
        for spec in Specialty.objects.all():
            specialities_amount[spec] = Vacancy.objects.filter(specialty=spec).count()
        context['specialities_amount'] = specialities_amount
        company_amount = {}
        for comp in Company.objects.all():
            company_amount[comp] = Vacancy.objects.filter(company=comp).count()
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
        return Vacancy.objects.filter(specialty__code=self.kwargs['field'])

    def get_context_data(self, **kwargs):
        context = super(VacanciesByCatView, self).get_context_data(**kwargs)
        context['specialty'] = Specialty.objects.get(code=self.kwargs['field'])
        return context


class AllVacanciesView(ListView):
    model = Vacancy
    template_name = 'jum/vacancies.html'
    context_object_name = 'vacancies'


class VacancyView(DetailView):
    model = Vacancy
    template_name = 'jum/vacancy.html'


def custom_handler404(request, exception):
    return HttpResponseNotFound('Страница не найдена, ошибка 404')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')
