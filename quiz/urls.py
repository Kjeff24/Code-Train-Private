from django.urls import path
from .views import quiz_view, quiz_data_view, save_quiz_view, quiz_list_view, quizResult

urlpatterns = [
    path('course/<str:pk2>/quiz/', quiz_list_view, name='main-view'),
    path('course/<str:pk2>/quiz/<pk>/', quiz_view, name='quiz-view'),
    path('course/<str:pk2>/quiz/<pk>/save/', save_quiz_view, name='save-view'),
    path('course/<str:pk2>/quiz/<pk>/data/', quiz_data_view, name='quiz-data-view'),
    path('course/grade-book/<pk>/', quizResult, name='quiz-result'),
]