from django.urls import path
from .views import TaskListCreateView, TaskDetailView, TodayTasksListView

urlpatterns = [
    ## for create and list tasks
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    ## for delete update and get tasks
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    ## for retrieve all todays tasks
    path('today-tasks/', TodayTasksListView.as_view(), name='today-tasks-list'),
]
