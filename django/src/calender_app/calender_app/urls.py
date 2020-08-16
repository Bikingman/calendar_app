
from django.contrib import admin
from django.urls import path, include
from calender import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('calender.urls')),
         ]