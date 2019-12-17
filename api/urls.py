from django.urls import path

from .views import TutorialList, TutorialDetail

urlpatterns = [
    path('', TutorialList.as_view(), name='tutorials-list'),
    # path('<int:id>', TutorialDetail.as_view(), name='tutoral-detail')
]