from django.contrib import admin
from django.urls import path
from . import views

app_name = 'tutorials'

urlpatterns = [

    # http://localhost:5000/
    path('', views.TutorialListView.as_view(), name='home-page'),
    path('tutorial', views.TutorialDetailView.as_view(), name='tutorial-detail-page'),
    path('create', views.TutorialCreateView.as_view(), name='create-tutorial-page'),

]