from django.urls import path 
from . import views

urlpatterns = [
    path('todos/', views.GetTodoListAPIView.as_view(), name='todo-list'),
    path('todo/<str:id>/', views.TodoDetailAPIView.as_view(), name='todo'),
]