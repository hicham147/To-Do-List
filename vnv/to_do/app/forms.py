from django import forms
from .models import Task

class AddTaskForm(forms.ModelForm):
    body =  forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))
    class Meta:
        model = Task
        fields = ('body',)
        
      
class UpdateForm(forms.ModelForm):
    body =  forms.CharField(widget= forms.TextInput())
    class Meta:
        model = Task
        fields = ('body',)  
    
        