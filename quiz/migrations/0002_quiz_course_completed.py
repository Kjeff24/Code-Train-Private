# Generated by Django 4.2.4 on 2023-09-18 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='course_completed',
            field=models.BooleanField(default=False),
        ),
    ]
