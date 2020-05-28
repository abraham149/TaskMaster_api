# api/views.py
from rest_framework import generics


from tasks import models
from . import serializers
from rest_framework import permissions

from api.permissions import IsOwnerOrReadOnly

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser



class ListTask(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    #queryset = models.Task.objects.filter(owner = request.user)
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer
    
    def get_queryset(self, *args, **kwargs):
        return models.Task.objects.all().filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class DetailTask(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]


    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer