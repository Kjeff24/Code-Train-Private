# Generated by Django 4.2.4 on 2023-09-18 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_quiz_course_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='course_completed',
        ),
    ]
