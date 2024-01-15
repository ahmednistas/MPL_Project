from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView


@login_required
def home(request):
    return render(request, "tasks/home.html")

'''
class CustomLoginView(LoginView):
    template_name = 'login/login.html'
    success_url = 'home'  # Redirect to the home view in the tasks app

login_view = login_required(CustomLoginView.as_view())

# Create your views here.
'''