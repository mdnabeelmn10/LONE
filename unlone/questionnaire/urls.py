from django.urls import path
from . import views

urlpatterns = [
    path('', views.questionnaire_view, name='questionnaire'),
    path('ok/',views.ok,name='ok'),
    path('mediocre/',views.mid,name='mid'),
    path('severe/',views.severe,name='severe'),
]
