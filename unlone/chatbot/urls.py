from django.urls import path
from . import views
from .views import chatbot_api

urlpatterns = [
    path('', chatbot_api, name='chatbot_api'),
    path('chat/', views.chatbot_view, name='chatbot'),
]

