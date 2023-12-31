from django.db import models
from myapp.models import User
# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=255, unique=True)
    course_image = models.ImageField(upload_to='images/', null=True, blank=True)
    heading = models.TextField()
    version = models.CharField(max_length=50)
    tutor = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField()  # Storing requirements as comma-separated values
    curriculum = models.TextField() 
    compiler = models.TextField(null=True, blank=True)# Storing curriculum as comma-separated values

    def __str__(self):
        return self.title
    

# Resources model allows employers to add resources based on course
class Resource(models.Model):
    FILE_TYPES = (
        ('pdf', 'PDF'),
        ('image', 'Image'),
        ('audio', 'Audio'),
        ('video', 'Video'),
        ('link', 'link'),
    )
    
    name = models.CharField(max_length=30)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.TextField()
    file_type = models.CharField(max_length=20, choices=FILE_TYPES, default="null")
    youtubeLink = models.TextField(blank=True)
    file = models.FileField(upload_to='resources/', blank=True)
    created  = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}-{self.course}-{self.file_type}"


class UserCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    course_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} - {self.course.title}"