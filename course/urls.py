from django.urls import path
from .views import coursePage, programme, previewPdf, downloadVideoFile, coursePageAbout, coursePageContact, resourcePage

urlpatterns = [
    path('course_page/', coursePage, name='course-page'),
    path('course_page/contact/', coursePageContact, name='course-page-contact'),
    path('course_page/about/', coursePageAbout, name='course-page-about'),
    path('course_page/programme/<str:pk>', programme, name='programme-page'), 
    path('course_page/programme/<str:pk>/resource', resourcePage, name='resource-page'), 
    path('preview_pdf/<int:pk>/', previewPdf, name='preview_pdf'),
    path('download/<int:pk>/', downloadVideoFile, name='download_video')
]