from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect


class LoginNotRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        return super().dispatch(request, *args, **kwargs)


class BaseForUserWithCompanyMixin:
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(request.user, 'company'):
            return HttpResponseRedirect('/company-start/')
        return super().dispatch(request, *args, **kwargs)


class ForUserWithCompanyMixin(LoginRequiredMixin, BaseForUserWithCompanyMixin):
    pass


class BaseForUserWithoutCompany:
    def dispatch(self, request, *args, **kwargs):
        if hasattr(request.user, 'company'):
            return HttpResponseRedirect('/company-edit/')
        else:
            return super().dispatch(request, *args, **kwargs)


class ForUserWithoutCompany(LoginRequiredMixin, BaseForUserWithoutCompany):
    pass


class BaseForUserWithVacancyMixin:
    def dispatch(self, request, *args, **kwargs):
        if hasattr(request.user.company, 'vacancies'):
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/vacancy-create/')


class ForUserWithVacancyMixin(LoginRequiredMixin, BaseForUserWithCompanyMixin, BaseForUserWithVacancyMixin):
    pass
