from django.urls import path
from . import views

app_name = 'tutorials'

urlpatterns = [

    # http://localhost:5000/
    path('', views.homepage, name='homepage'),
]