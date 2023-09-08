# Generated by Django 4.2.4 on 2023-08-25 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('version', models.CharField(max_length=50)),
                ('tutor', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('requirements', models.TextField()),
                ('curriculum', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, max_length=50)),
                ('file_type', models.CharField(choices=[('pdf', 'PDF'), ('image', 'Image'), ('audio', 'Audio'), ('video', 'Video'), ('link', 'link')], default='null', max_length=10)),
                ('youtubeLink', models.TextField(blank=True)),
                ('file', models.FileField(blank=True, upload_to='resources/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user_download_count', models.PositiveIntegerField(default=0)),
                ('user_email_sent', models.PositiveIntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
            ],
        ),
    ]