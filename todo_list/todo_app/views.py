from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TaskSerializer
from .models import Task


class apiOverview(APIView):
	def get(self, request, format=None):
		api_urls = {
			'List':'/task-list/',
			'Detail View':'/task-detail/<str:pk>/',
			'Create':'/task-create/',
			'Update':'/task-update/<str:pk>/',
			'Delete':'/task-delete/<str:pk>/',
			}
		return Response(api_urls)


class taskList(APIView):
	def get(self, request, format=None):
		tasks = Task.objects.all().order_by('-id')
		serializer = TaskSerializer(tasks, many=True)
		return Response(serializer.data)



class taskDetail(APIView):
	def get(self, request, pk, format=None):
		tasks = Task.objects.get(id=pk)
		serializer = TaskSerializer(tasks, many=False)
		return Response(serializer.data)



class taskCreate(APIView):
	def post(self, request, format=None):
		serializer = TaskSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
		return Response(serializer.data)



class taskUpdate(APIView):
	def put(self, request, pk, format=None):
		task = Task.objects.get(id=pk)
		serializer = TaskSerializer(task, data=request.data)
		if serializer.is_valid():
			serializer.save()
		return Response(serializer.data)


class taskDelete(APIView):
	def delete(self, request, pk, format=None):
		task = Task.objects.get(id=pk)
		task.delete()
		return Response('Item succsesfully deleted!')



