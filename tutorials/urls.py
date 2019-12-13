from django.urls import path
from . import views

app_name = 'tutorials'

urlpatterns = [

    # http://localhost:5000/
    path('', views.TutorialListView.as_view(), name='homepage'),
    path('tutorial', views.TutorialDetailView.as_view(), name='tutorialpage')
]