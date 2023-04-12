from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homepage, name='home'),
    path('reply/', views.replypage, name='reply'),
    path('replylogin/',views.replylogin,name='replylogin'),
]