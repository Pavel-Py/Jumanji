# Generated by Django 4.0.2 on 2022-03-07 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jum', '0002_rename_name_company_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='published_at',
            field=models.CharField(max_length=16),
        ),
    ]
