# Generated by Django 4.0.2 on 2022-03-18 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jum', '0013_alter_company_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(upload_to='company'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='picture',
            field=models.ImageField(upload_to='specialization'),
        ),
    ]
