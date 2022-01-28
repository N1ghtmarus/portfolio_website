from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('projects', views.projects, name="projects"),
    # path('contacts', views.contacts, name="contacts"),
    path('contacts_test', views.contacts_test, name="contacts_test"),
    path('say_thanks', views.say_thanks, name="say_thanks"),

    #paths for ru languange
    path('home_ru', views.home_ru, name="home_ru"),
    path('about_ru', views.about_ru, name="about_ru"),
    path('projects_ru', views.projects_ru, name="projects_ru"),
    path('contacts_test_ru', views.contacts_test_ru, name="contacts_test_ru"),
    path('say_thanks_ru', views.say_thanks_ru, name="say_thanks_ru"),
]

