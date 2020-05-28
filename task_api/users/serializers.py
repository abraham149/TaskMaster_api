# users/serializers.py
from rest_framework import serializers
from . import models
from tasks.models import Task
from api.permissions import IsOwnerOrReadOnly



class UserSerializer(serializers.ModelSerializer):
    #tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())
    class Meta:
        model = models.CustomUser
        fields = ('email', 'username', 'name', 'password')
        
        extra_kwargs = {
            'password': {'write_only': True}
        }
        