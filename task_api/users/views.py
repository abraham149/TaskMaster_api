# users/views.py
from rest_framework import generics

from django.views.decorators.csrf import csrf_exempt
from . import models
from django.http import HttpResponse, JsonResponse

from . import serializers
from rest_framework.parsers import JSONParser



class UserListView(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer


class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer


@csrf_exempt
def user_profile(request):
    user = request.user
    print(user)
    if user is None:
        return HttpResponse(status = 404)

    if request.method == 'GET':
        serializer = serializers.UserSerializer(user)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = serializers.UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)