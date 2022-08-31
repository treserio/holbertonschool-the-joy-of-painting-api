from django.shortcuts import render
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework import filters


from .models import HexValues
from .serializers import HexValuesSer

class hex_values(ListAPIView):
    queryset = HexValues.objects.all()
    serializer_class = HexValuesSer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = [
        'index',
        'color',
        'hex'
    ]
    ordering_fields = [
        'index',
        'color',
    ]
    search_fields = [
        'color',
    ]
