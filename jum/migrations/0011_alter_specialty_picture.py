# Generated by Django 4.0.2 on 2022-03-18 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jum', '0010_alter_specialty_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialty',
            name='picture',
            field=models.ImageField(upload_to='specialization/'),
        ),
    ]
