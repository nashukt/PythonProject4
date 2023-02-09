from . import views
from django.urls import path

urlpatterns = [

    path('', views.demo, name='demo'),
    # path('about/',views.about,name='about'),
    # path('gallery/',views.gallery,name='gallery'),
    # path('login/',views.login,name='login'),
    # path('contact/',views.contact,name='contact'),
]
