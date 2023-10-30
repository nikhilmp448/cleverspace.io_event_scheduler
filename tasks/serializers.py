from rest_framework import serializers, generics, permissions
from .models import Task, IndividualTask

class IndividualTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualTask
        fields = '__all__'
        extra_kwargs = {
            'task': {'required': False}
        }

class TaskSerializer(serializers.ModelSerializer):
    individual_tasks = IndividualTaskSerializer(many=True, required=False)

    class Meta:
        model = Task
        fields = '__all__'
        extra_kwargs = {
            'user': {'required': False}
        }

    def create(self, validated_data):
        individual_tasks_data = validated_data.pop('individual_tasks', [])
        task = Task.objects.create(**validated_data)

        for individual_task_data in individual_tasks_data:
            IndividualTask.objects.create(task=task, **individual_task_data)

        return task