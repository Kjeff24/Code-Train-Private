from django.shortcuts import render, redirect
from .models import Course, Resource
import json
from django.db.models import Q
from django.http import StreamingHttpResponse
from urllib.parse import urlencode
from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.
@login_required(login_url='login')
def coursePage(request):
    page = "logged_page"
    courses = Course.objects.all()
    context ={"page":page, 'courses':courses}
    return render(request, 'course_page/course_page.html', context)

@login_required(login_url='login')
def coursePageAbout(request):
    return render(request, 'course_page/course_page_about.html')

@login_required(login_url='login')
def coursePageContact(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstname')
        other_name = request.POST.get('othernames')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        from_message = request.POST.get('textarea-message')
        
        send_mail(
            subject="Message from Contact Form",
            message=f'Name: {first_name} {other_name}\nPhone: {phone}\nEmail: {email}\n\nMessage: {from_message}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        messages.add_message(request, messages.SUCCESS,
                                         'Your email has been successfully sent')  
        return redirect('contact') 

    return render(request, 'course_page/course_page_contact.html')


@login_required(login_url='login')
def programme(request, pk):
    q = request.GET.get('q', '')
    page = "programme_page"
    course = Course.objects.get(pk=pk)
    curriculum_list = json.loads(course.curriculum.replace("'", "\""))
    requirement_list = json.loads(course.requirements.replace("'", "\""))
    
    files_by_type = {
        'pdf': 'pdf_files',
        'image': 'image_files',
        'audio': 'audio_files',
        'video': 'video_files',
        'link': 'youtube_links',
    }
    
    file_types = files_by_type.keys()
    resources = {}
    
    for file_type in file_types:
        resources[files_by_type[file_type]] = Resource.objects.filter(
            Q(name__icontains=q) |
            Q(description__icontains=q) |
            Q(file__icontains=q) |
            Q(youtubeLink__icontains=q) |
            Q(file_type__icontains=q),
            file_type=file_type,
            course=course
        ).order_by('-updated')
    
    context ={ 
        'page': page,
        'course':course, 
        **resources,
        'curriculum_list': curriculum_list,
        'requirement_list': requirement_list,
        }
    return render(request, 'course_page/programme.html', context)

# Preview pdf
def previewPdf(request, pk):
    file = Resource.objects.get(id=pk)
    # pdf is streamed in chunks, rather than loading entire file
    def file_iterator():
        with open(file.file.path, 'rb') as f:
            for chunk in iter(lambda: f.read(8192), b''):
                yield chunk
    # use StreamingHttpResponse to load pdf content
    response = StreamingHttpResponse(
        file_iterator(), content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="{}"'.format(
        urlencode({'': file.file.name}))
    return response



def downloadVideoFile(request, pk):
    resource = Resource.objects.get(pk=pk)
    file_path = resource.file.path
    file_name = resource.file.name.split('/')[-1]  # Extract the file name

    response = FileResponse(open(file_path, 'rb'), content_type='video/mp4')
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    return response

