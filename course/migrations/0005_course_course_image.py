# Generated by Django 4.2.4 on 2023-08-27 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_remove_resource_user_download_count_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_image',
            field=models.FileField(blank=True, upload_to='resources/'),
        ),
    ]