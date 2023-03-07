from django.urls import path
from . import views

urlpatterns = [
    path('set', views.setcookie, name='set'),
    path('get', views.getcookie, name='get'),
    path('del',views.delcookie, name='del'),
    path('session_store', views.session_store, name='session_store'),
    path('session_get', views.session_get, name='session_get'),
    path('session_del', views.session_del, name='session_del'),
]