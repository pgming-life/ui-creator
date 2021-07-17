from django.db import models
from rest_framework import serializers

# model
class BaseModel(models.Model):
    name_key = models.CharField(max_length=10, verbose_name='name_key')
    stack_key = models.CharField(max_length=20, verbose_name='stack_key')
    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    left = models.PositiveIntegerField()
    top = models.PositiveIntegerField()

# serializer
class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseModel
        fields = [
            'id',
            'name_key',
            'stack_key',
            'width',
            'height',
            'left',
            'top',
        ]
