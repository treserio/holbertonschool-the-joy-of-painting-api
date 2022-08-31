from django.shortcuts import render
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework import filters


from .models import Colors, HexValues, PicInfo
from .serializers import ColorsSeri, HexValuesSeri, PicInfoSeri

class hex_values(ListAPIView):
    queryset = HexValues.objects.all()
    serializer_class = HexValuesSeri
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
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

class pic_info(ListAPIView):
    queryset = PicInfo.objects.all()
    serializer_class = PicInfoSeri
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_fields = {
        'episode': ['exact', 'icontains'],
        'painting_index': ['lt', 'gt', 'lte', 'gte', 'exact'],
        'painting_title': ['exact', 'icontains'],
        'season': ['lt', 'gt', 'lte', 'gte', 'exact'],
        'episode_num': ['lt', 'gt', 'lte', 'gte', 'exact'],
        'num_colors': ['lt', 'gt', 'lte', 'gte', 'exact'],
        'air_date': ['lt', 'gt', 'lte', 'gte', 'exact'],
    }
    ordering_fields = [
        'episode',
        'painting_index',
        'painting_title',
        'season',
        'episode_num',
        'num_colors',
        'air_date'
    ]
    search_fields = [
        'episode',
        'painting_index',
        'painting_title',
        'season',
        'episode_num',
        'num_colors',
        'air_date'
    ]

class colors(ListAPIView):
    queryset = Colors.objects.all()
    serializer_class = ColorsSeri
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_fields = [
        'episode',
        'black_gesso',
        'bright_red',
        'burnt_umber',
        'cadmium_yellow',
        'dark_sienna',
        'indian_red',
        'indian_yellow',
        'liquid_black',
        'liquid_clear',
        'midnight_black',
        'phthalo_blue',
        'phthalo_green',
        'prussian_blue',
        'sap_green',
        'titanium_white',
        'van_dyke_brown',
        'yellow_ochre',
        'alizarin_crimson',
    ]
    ordering_fields = [
        'episode'
    ]
    search_fields = [
        'episode'
    ]
