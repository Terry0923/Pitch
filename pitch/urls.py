from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='pitch-home'),
    path('about/',views.about,name='pitch-about'),
]
