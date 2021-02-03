from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('contact',views.contact, name='contact'),
    path('about',views.about, name='about'),
    path('register',views.register, name='register'),
    path('login',views.login, name='login'),
    path('desc/<slug:uname>/<int:id>/',views.desc, name='desc'),
    path('end',views.end, name='end')
]