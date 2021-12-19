from django.urls import path
from django.conf.urls import url



from django.contrib import admin
from django.urls import path
from  upload_csv import views

urlpatterns = [
   # path('admin/', admin.site.urls),
    path('', views.main),
    
]
