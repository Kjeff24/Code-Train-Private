# Generated by Django 4.2.4 on 2023-09-18 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0012_alter_course_course_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_completed',
            field=models.BooleanField(default=False),
        ),
    ]