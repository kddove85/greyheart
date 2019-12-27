from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about_us', views.about_us, name='about_us'),
    path('available_greys', views.available_greys, name='available_greys'),
    path('adoption', views.get_adoption_form, name='adoption'),
    path('events', views.events, name='events'),
]

