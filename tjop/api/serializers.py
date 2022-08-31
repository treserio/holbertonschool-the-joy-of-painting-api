from rest_framework import serializers
from . import models

class ColorsSeri(serializers.ModelSerializer):
    class Meta:
        model = models.Colors
        fields = [
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

class HexValuesSeri(serializers.ModelSerializer):
    class Meta:
        model = models.HexValues
        fields = [
            'index',
            'color',
            'hex'
        ]

class PicInfoSeri(serializers.ModelSerializer):
    class Meta:
        model = models.PicInfo
        fields = [
            'index',
            'episode',
            'painting_index',
            'img_src',
            'painting_title',
            'season',
            'episode_num',
            'num_colors',
            'youtube_src',
            'air_date'
        ]
