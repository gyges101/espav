from .views import *
from django.urls import path

app_name = 'app'


urlpatterns = [
    path('', home, name='home'),
    path('presentation', presentation, name='presentation'),
    path('equipement', equipement, name='equipement'),
    path('inscription', inscription, name='inscription'),
    path('press', press, name='press'),
    path('prodvisuel', prodvisuel, name='prodvisuel'),
    path('allform', allform, name='allform'),
    path('agenda', agenda, name='agenda'),
    path('faq', faq, name='faq'),
    path('contact', contact, name='contact'),
]
