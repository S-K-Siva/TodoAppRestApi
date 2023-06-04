from django.forms import ModelForm
from .models import Task,Tags
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

class TagForm(ModelForm):
    class Meta:
        model = Tags 
        fields = '__all__'


