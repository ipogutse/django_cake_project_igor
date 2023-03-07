from django.urls import path
from . import views

urlpatterns = [
    path('studentinfo', views.studentinfo, name='studentinfo'),
    path('qset', views.qset, name='qset'),
]

