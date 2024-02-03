from django.urls import path, include

urlpatterns = [
    path('app/', include('todo_list.urls'))
]
