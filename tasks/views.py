from rest_framework import generics, permissions
from .models import Task,IndividualTask
from django.utils import timezone
from .serializers import TaskSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user)

    def perform_create(self, serializer):
        individual_tasks_data = serializer.validated_data.pop('individual_tasks', [])
        task = serializer.save(user=self.request.user)

        for individual_task_data in individual_tasks_data:
            IndividualTask.objects.create(task=task, **individual_task_data)

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user)

    def perform_update(self, serializer):
        # Extract and remove the individual_tasks field from the data
        individual_tasks_data = serializer.validated_data.pop('individual_tasks', [])

        task = serializer.save(user=self.request.user)

        # Delete existing individual tasks and recreate them
        task.individual_tasks.all().delete()
        for individual_task_data in individual_tasks_data:
            task.individual_tasks.create(**individual_task_data)

class TodayTasksListView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        today = timezone.now().date()
        return Task.objects.filter(user=user, scheduled_date__date=today)
