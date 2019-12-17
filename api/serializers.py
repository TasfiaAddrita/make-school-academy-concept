from rest_framework.serializers import ModelSerializer
from tutorials.models import Tutorial, Module

class TutorialSerializer(ModelSerializer):
    class Meta:
        model = Tutorial
        fields = '__all__'

class TutorialDetailSerializer(ModelSerializer):
    class Meta:
        model = Tutorial
        fields = '__all__'