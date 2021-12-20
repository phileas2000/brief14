from django.urls import path
from django.conf.urls import url



from django.contrib import admin
from django.urls import path
from  data_view import views

urlpatterns = [
    path('', views.main),
    
]
