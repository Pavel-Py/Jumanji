# Generated by Django 4.0.2 on 2022-03-18 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jum', '0012_alter_specialty_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(upload_to='media'),
        ),
    ]
