from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from course.models import Course

# Create your views here.
def home(request):
    return render(request, 'front_page/home.html')

def courses(request):
    courses = Course.objects.all()
    context ={'courses':courses}
    return render(request, 'front_page/courses.html', context)

def about(request):
    return render(request, 'front_page/about.html')

def contact(request):
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

    return render(request, 'front_page/contact.html')

def cart(request):
    return render(request, 'front_page/cart.html')

# url does not exist
def custom_404(request):
    return render(request, 'front_page/404.html', status=404)

