# Generated by Django 4.2.4 on 2023-08-27 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_alter_course_course_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
