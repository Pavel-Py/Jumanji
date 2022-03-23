from django.contrib.auth.models import User
from django.db import models


class Company(models.Model):
    title = models.CharField(max_length=32)
    location = models.CharField(max_length=32)
    logo = models.ImageField(upload_to='company')
    description = models.TextField()
    employee_count = models.IntegerField()
    owner = models.OneToOneField(User, related_name='company', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '%s %s %s' % (self.title, self.location, self.description)


class Specialty(models.Model):
    code = models.CharField(max_length=16)
    title = models.CharField(max_length=32)
    picture = models.ImageField(upload_to='specialization')

    def __str__(self):
        return '%s %s' % (self.title, self.code)


class Vacancy(models.Model):
    title = models.CharField(max_length=32)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")
    skills = models.TextField()
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.CharField(max_length=16)

    def __str__(self):
        return '%s %s %s' % (self.title, self.skills, self.description)


class Application(models.Model):
    written_username = models.CharField(max_length=32)
    written_phone = models.CharField(max_length=16)
    written_cover_letter = models.TextField()
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name="applications")
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="applications")
