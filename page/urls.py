from django.urls import path
from .views import home, about, contact, welcome

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('welcome/', welcome, name='welcome'),
]