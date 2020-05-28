# api/serializers.py
from rest_framework import serializers
from tasks import models


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        fields = (
            'id',
            'titulo',
            'descripcion',
            'lugar',
            'fecha',
            'hora',
            'owner',
        )
        model = models.Task