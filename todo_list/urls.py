from django.urls import path
from . import views
from .views import TaskListCreate, TaskRetrieveUpdateDestroy

urlpatterns = [
    path('tasks/', TaskListCreate.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroy.as_view(), name='task-retrieve-update-destroy'),
    path('get_all/', views.get_all, name='get-all-task'),
    path('add/', views.add_task, name='add-task'),
    path('get/<int:id>/', views.get_by_id, name='get-task-by-id'),
    path('update/<int:id>/', views.update, name='update-task'),
    path('delete/<int:id>/', views.delete, name='delete-task'),
]
