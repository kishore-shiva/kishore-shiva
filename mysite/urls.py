from django.contrib import admin
from django.urls import include, path
from polls.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/',index),
]