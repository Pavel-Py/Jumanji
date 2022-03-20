from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Row, Column, Layout
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from jum.models import Company, Vacancy, Application


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Зарегистрироваться'))
        self.fields['username'].label = 'Логин'
        self.fields['password1'].label = 'Пароль'
        self.fields['password2'].label = 'Повтор пароля'
        self.fields['first_name'].label = 'Имя'
        self.fields['last_name'].label = 'Фамилия'
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''


class LoginUserForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Войти'))
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'


class CompanyCreate(forms.ModelForm):
    logo = forms.ImageField()

    class Meta:
        model = Company
        fields = ['title', 'location', 'logo', 'description', 'employee_count']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.fields['title'].label = 'Название'
        self.fields['location'].label = 'Находимся'
        self.fields['logo'].label = 'Эмблема'
        self.fields['description'].label = 'Описание'
        self.fields['employee_count'].label = 'Количество сотрудников'
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-md-6 mb-0', data_name="whatever"),
                Column('logo', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('employee_count', css_class='form-group col-md-6 mb-0'),
                Column('location', css_class='form-group col-md-6 mb-0'),
            ),
            'description'
        )


class VacancyCreate(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'specialty', 'skills', 'description', 'salary_min', 'salary_max']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Добавить'))
        self.fields['title'].label = 'Название'
        self.fields['specialty'].label = 'Специализация'
        self.fields['skills'].label = 'Скилы'
        self.fields['description'].label = 'Описание'
        self.fields['salary_min'].label = 'Зарплата от'
        self.fields['salary_max'].label = 'Зарплата до'
        self.helper.layout = Layout(
            Row(
                Column('title',  label='название', css_class='form-group col-md-6 mb-0', data_name="whatever"),
                Column('specialty', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('salary_min', css_class='form-group col-md-6 mb-0'),
                Column('salary_max', css_class='form-group col-md-6 mb-0'),
                css_class='form-row',
            ),
            'skills',
            'description'
        )


class ApplicationCreate(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['written_username', 'written_phone', 'written_cover_letter']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Добавить'))
        self.helper.form_class = 'form-horizontal'
