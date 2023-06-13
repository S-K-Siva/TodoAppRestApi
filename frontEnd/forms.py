from django.forms import ModelForm,forms
from django import forms
from .models import Task,Tags
class TaskForm(ModelForm,forms.Form):
    new_tag = forms.CharField(label="Tag",max_length=200)
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['tags']

class TagForm(ModelForm):
    class Meta:
        model = Tags 
        fields = '__all__'


