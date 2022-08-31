from rest_framework import serializers
from . import models

class HexValuesSer(serializers.ModelSerializer):
    class Meta:
        model = models.HexValues
        fields = [
            'index',
            'color',
            'hex'
        ]
