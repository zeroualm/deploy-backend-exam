from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from .models import Task,Category
from .serializers import *
from rest_framework import viewsets,status
from rest_framework.response import Response

def health_check(request):
        """Une vue simple qui renvoie un statut de succès."""
        return JsonResponse({"status": "ok", "message": "API is healthy"})

class CategoryViewSet(viewsets.ViewSet):
    
    serializer_class = CategorySerializer

    # GET
    def list(self, request):
        queryset = Category.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        if serializer.data :
            return Response(serializer.data,status=status.HTTP_200_OK)
        else : 
            return Response({"message":"Aucune catégorie n'a été trouvé"},status=status.HTTP_404_NOT_FOUND)
        
    # POST
    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskViewSet(viewsets.ViewSet):

    serializer_class = TaskSerializer
    
    # GET
    def list(self, request):
        queryset = Task.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        if serializer.data :
            return Response(serializer.data,status=status.HTTP_200_OK)
        else : 
            return Response({"message":"Aucune tâche n'a été trouvé"},status=status.HTTP_404_NOT_FOUND)
        
    # POST
    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    # PATCH
    def partial_update(self, request, pk=None):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE
    def destroy(self, request, pk=None):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

