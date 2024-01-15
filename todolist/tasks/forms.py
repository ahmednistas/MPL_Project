import django.forms
from django.forms import ModelForm, forms
from .models import Task, User

'''
class LoginForm(forms.Form):
    UEmail = django.forms.EmailField(required=True, max_length=150, label="Your Email ")
    UPassword = django.forms.CharField(required=True, max_length=150, label="Password ")
'''
'''
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
'''
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['TName', 'DueDate', 'Repeat', 'Status', 'Priority', 'Category', 'Description']

'''
class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['UName','UEmail','UPassword']
'''

class add_taskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['TName','DueDate','Repeat','Status','Priority']
