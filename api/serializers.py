from rest_framework.serializers import ModelSerializer
from frontEnd.models import Task,Tags 

class TaskSerializers(ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

class TagSerializers(ModelSerializer):
    class Meta:
        model = Tags 
        fields = "__all__"
