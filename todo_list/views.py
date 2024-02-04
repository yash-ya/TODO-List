from rest_framework import generics
import json
from .models import Task
from .serializers import TaskSerializer
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from .common_helper import CommonHelper

class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

@csrf_exempt
def get_all(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serialized_data = [CommonHelper.serialize(task) for task in tasks]
        return JsonResponse(serialized_data, safe=False)
    else:
        return HttpResponseNotAllowed(['GET'])
    
@csrf_exempt
def add_task(request):
    if request.method == 'POST':
        task = CommonHelper.deserialize(request.body)
        if task is None:
            return JsonResponse({'error': 'Invalid data'}, status=400)
        task.save()
        serialized_task = CommonHelper.serialize(task)
        return JsonResponse(serialized_task, status=201)
    else:
        return HttpResponseNotAllowed(['POST'])

@csrf_exempt
def get_by_id(request, id):
    if request.method == 'GET':
        try:
            task = Task.objects.get(id=id)
        except Task.DoesNotExist:
            return JsonResponse({'error': 'Data does not exist for this id'}, status=400)
        serialized_task = CommonHelper.serialize(task)
        return JsonResponse(serialized_task, status=200)
    else:
        return HttpResponseNotAllowed(['GET'])

@csrf_exempt
def update(request, id):
    if request.method == 'PUT':
        try:
            task = Task.objects.get(id=id)
        except Task.DoesNotExist:
            return JsonResponse({'error': 'Data does not exist for this id'}, status=400)
        updated_task = CommonHelper.deserialize(request.body)
        if updated_task is None:
            return JsonResponse({'error': 'Invalid data'}, status=400)
        task.title = updated_task.title if task.title != updated_task.title else task.title
        task.description = updated_task.description if task.description != updated_task.description else task.description
        task.completed = updated_task.completed if task.completed != updated_task.completed else task.completed
        task.save()
        serialized_task = CommonHelper.serialize(task)
        return JsonResponse(serialized_task, status=200)
    else:
        return HttpResponseNotAllowed(['PUT'])

@csrf_exempt
def delete(request, id):
    if request.method == 'DELETE':
        try:
            task = Task.objects.get(id=id)
        except Task.DoesNotExist:
            return JsonResponse({'error': 'Data does not exist for this id'}, status=400)
        task.delete()
        return JsonResponse({'message': 'Task deleted successfully'}, status=204)
    else:
        return HttpResponseNotAllowed(['DELETE'])
