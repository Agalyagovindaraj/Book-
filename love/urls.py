"""
URL configuration for valentinesite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('yes/', views.yes_page, name='yes'),
    path('final/', views.final_page, name='final'),
    path('sorry/', views.sorry_page, name='sorry'),
    path('fights/', views.fights, name='fights'),
    path('love-everyday/', views.love_everyday, name='love_everyday'),
    path('mood-swings/', views.mood_swings, name='mood_swings'),
    path("final/", views.final_promise, name="final_promise"),
     path('journey/', views.journey, name='journey'),
     path('next1/', views.next1, name='next1'),  
     path("proposal/", views.proposal, name="proposal"),

]

