from django.urls import path
from . import views
from .views import home,add_task, important, all_tasks, delete_task, edit_task

urlpatterns = [

    path('tasks/home/', home, name='home'),
    path('tasks/important/', important, name='important'),
    path('tasks/all_tasks/', all_tasks, name='all_tasks'),
    path('add_task/', add_task, name='add_task'),
    #path('search_bar/', search_bar, name='search_bar'),
    path('delete_task/<int:pk>/', delete_task, name='delete_task'),
    path('edit_task/<int:pk>/', edit_task, name='edit_task'),
]
