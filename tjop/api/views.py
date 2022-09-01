from django.shortcuts import render
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework import filters
import json


from .models import Colors, HexValues, PicInfo, Subjects
from .serializers import ColorsSeri, HexValuesSeri, JoinTableSeri, PicInfoSeri, SubjectsSeri

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
        'alizarin_crimson',
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
    ]
    ordering_fields = [
        'episode'
    ]
    search_fields = [
        'episode'
    ]

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

class join_table(ListAPIView):
        # color_list = [
        #     'alizarin_crimson',
        #     'black_gesso',
        #     'bright_red',
        #     'burnt_umber',
        #     'cadmium_yellow',
        #     'dark_sienna',
        #     'indian_red',
        #     'indian_yellow',
        #     'liquid_black',
        #     'liquid_clear',
        #     'midnight_black',
        #     'phthalo_blue',
        #     'phthalo_green',
        #     'prussian_blue',
        #     'sap_green',
        #     'titanium_white',
        #     'van_dyke_brown',
        #     'yellow_ochre',
        # ]
        # ###
        # #   perform queries and pair data together
        # ###
        # all_data = PicInfo.objects.all()
        # print('\nall_data\n', all_data.__dict__)
        # # used to create colors_used index for output
        # hexes = HexValues.objects.all().order_by('color')
        # print('\n', hexes.__dict__, '\n')
        # # print('\nhexes\n', hexes, '\n')
        # # print('\n'.join(h.color for h in hexes))
        # print(' '.join(color_list[0].split('_')).title())
        # print('wtf', hexes.filter(color=' '.join(color_list[0].split('_')).title()))

        # ###
        # #   create the colors_used value and store in each queried item
        # ###
        # for item in all_data:
        #     # print(item.liquid_clear, item.episode, item.img_src, item.barn)
        #     color_hexes = {}
        #     for i in range(len(color_list)):
        #         # print(item)
        #         # print('\ndundering\n', hexes.filter(color=' '.join(color_list[0].split('_')).title())[0].hex, '\n')
        #         if getattr(item.episode_colors, color_list[i]) == 1:
        #             color_hexes.update({' '.join(color_list[i].split('_')).title():
        #             hexes.filter(color=' '.join(color_list[i].split('_')).title())[0].hex
        #         })
        #     item.colors_used = str(color_hexes)
    queryset = PicInfo.objects.all()
    serializer_class = JoinTableSeri
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    # filterset_fields = {
    #     # PIC_INFO
    #     'episode': ['exact', 'icontains'],
    #     'painting_index': ['lt', 'gt', 'lte', 'gte', 'exact'],
    #     'painting_title': ['exact', 'icontains'],
    #     'season': ['lt', 'gt', 'lte', 'gte', 'exact'],
    #     'episode_num': ['lt', 'gt', 'lte', 'gte', 'exact'],
    #     'num_colors': ['lt', 'gt', 'lte', 'gte', 'exact'],
    #     'air_date': ['lt', 'gt', 'lte', 'gte', 'exact'],
    #     # COLORS
    #     'alizarin_crimson': ['exact'],
    #     'black_gesso': ['exact'],
    #     'bright_red': ['exact'],
    #     'burnt_umber': ['exact'],
    #     'cadmium_yellow': ['exact'],
    #     'dark_sienna': ['exact'],
    #     'indian_red': ['exact'],
    #     'indian_yellow': ['exact'],
    #     'liquid_black': ['exact'],
    #     'liquid_clear': ['exact'],
    #     'midnight_black': ['exact'],
    #     'phthalo_blue': ['exact'],
    #     'phthalo_green': ['exact'],
    #     'prussian_blue': ['exact'],
    #     'sap_green': ['exact'],
    #     'titanium_white': ['exact'],
    #     'van_dyke_brown': ['exact'],
    #     'yellow_ochre': ['exact'],
    #     # SUBJECTS
    #     'apple_frame': ['exact'],
    #     'aurora_borealis': ['exact'],
    #     'barn': ['exact'],
    #     'beach': ['exact'],
    #     'boat': ['exact'],
    #     'bridge': ['exact'],
    #     'building': ['exact'],
    #     'bushes': ['exact'],
    #     'cabin': ['exact'],
    #     'cactus': ['exact'],
    #     'circle_frame': ['exact'],
    #     'cirrus': ['exact'],
    #     'cliff': ['exact'],
    #     'clouds': ['exact'],
    #     'conifer': ['exact'],
    #     'cumulus': ['exact'],
    #     'deciduous': ['exact'],
    #     'diane_andre': ['exact'],
    #     'dock': ['exact'],
    #     'double_oval_frame': ['exact'],
    #     'farm': ['exact'],
    #     'fence': ['exact'],
    #     'fire': ['exact'],
    #     'florida_frame': ['exact'],
    #     'flowers': ['exact'],
    #     'fog': ['exact'],
    #     'framed': ['exact'],
    #     'grass': ['exact'],
    #     'guest': ['exact'],
    #     'half_circle_frame': ['exact'],
    #     'half_oval_frame': ['exact'],
    #     'hills': ['exact'],
    #     'lake': ['exact'],
    #     'lakes': ['exact'],
    #     'lighthouse': ['exact'],
    #     'mill': ['exact'],
    #     'moon': ['exact'],
    #     'mountain': ['exact'],
    #     'mountains': ['exact'],
    #     'night': ['exact'],
    #     'ocean': ['exact'],
    #     'oval_frame': ['exact'],
    #     'palm_trees': ['exact'],
    #     'path': ['exact'],
    #     'person': ['exact'],
    #     'portrait': ['exact'],
    #     'rectangle_3d_frame': ['exact'],
    #     'rectangular_frame': ['exact'],
    #     'river': ['exact'],
    #     'rocks': ['exact'],
    #     'seashell_frame': ['exact'],
    #     'snow': ['exact'],
    #     'snowy_mountain': ['exact'],
    #     'split_frame': ['exact'],
    #     'steve_ross': ['exact'],
    #     'structure': ['exact'],
    #     'sun': ['exact'],
    #     'tomb_frame': ['exact'],
    #     'tree': ['exact'],
    #     'trees': ['exact'],
    #     'triple_frame': ['exact'],
    #     'waterfall': ['exact'],
    #     'waves': ['exact'],
    #     'windmill': ['exact'],
    #     'window_frame': ['exact'],
    #     'winter': ['exact'],
    #     'wood_framed': ['exact'],
    # }
    # search_fields = [
    #     'episode',
    #     'painting_index',
    #     'painting_title',
    #     'season',
    #     'episode_num',
    #     'num_colors',
    #     'air_date'
    # ]
    # ordering_fields = [
    #     'episode',
    #     'painting_index',
    #     'painting_title',
    #     'season',
    #     'episode_num',
    #     'num_colors',
    #     'air_date'
    # ]

class pic_info(ListAPIView):
    queryset = PicInfo.objects.all()
    serializer_class = PicInfoSeri
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_fields = {
        'episode_colors__episode': ['exact', 'icontains'],
        'painting_index': ['lt', 'gt', 'lte', 'gte', 'exact'],
        'painting_title': ['exact', 'icontains'],
        'season': ['lt', 'gt', 'lte', 'gte', 'exact'],
        'episode_num': ['lt', 'gt', 'lte', 'gte', 'exact'],
        'num_colors': ['lt', 'gt', 'lte', 'gte', 'exact'],
        'air_date': ['lt', 'gt', 'lte', 'gte', 'exact'],
    }
    ordering_fields = [
        'episode_colors',
        'painting_index',
        'painting_title',
        'season',
        'episode_num',
        'num_colors',
        'air_date'
    ]
    search_fields = [
        'episode_colors',
        'painting_index',
        'painting_title',
        'season',
        'episode_num',
        'num_colors',
        'air_date'
    ]

class subj_view(ListAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectsSeri
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_fields = {
        'episode': ['exact', 'icontains'],
        'apple_frame': ['exact'],
        'aurora_borealis': ['exact'],
        'barn': ['exact'],
        'beach': ['exact'],
        'boat': ['exact'],
        'bridge': ['exact'],
        'building': ['exact'],
        'bushes': ['exact'],
        'cabin': ['exact'],
        'cactus': ['exact'],
        'circle_frame': ['exact'],
        'cirrus': ['exact'],
        'cliff': ['exact'],
        'clouds': ['exact'],
        'conifer': ['exact'],
        'cumulus': ['exact'],
        'deciduous': ['exact'],
        'diane_andre': ['exact'],
        'dock': ['exact'],
        'double_oval_frame': ['exact'],
        'farm': ['exact'],
        'fence': ['exact'],
        'fire': ['exact'],
        'florida_frame': ['exact'],
        'flowers': ['exact'],
        'fog': ['exact'],
        'framed': ['exact'],
        'grass': ['exact'],
        'guest': ['exact'],
        'half_circle_frame': ['exact'],
        'half_oval_frame': ['exact'],
        'hills': ['exact'],
        'lake': ['exact'],
        'lakes': ['exact'],
        'lighthouse': ['exact'],
        'mill': ['exact'],
        'moon': ['exact'],
        'mountain': ['exact'],
        'mountains': ['exact'],
        'night': ['exact'],
        'ocean': ['exact'],
        'oval_frame': ['exact'],
        'palm_trees': ['exact'],
        'path': ['exact'],
        'person': ['exact'],
        'portrait': ['exact'],
        'rectangle_3d_frame': ['exact'],
        'rectangular_frame': ['exact'],
        'river': ['exact'],
        'rocks': ['exact'],
        'seashell_frame': ['exact'],
        'snow': ['exact'],
        'snowy_mountain': ['exact'],
        'split_frame': ['exact'],
        'steve_ross': ['exact'],
        'structure': ['exact'],
        'sun': ['exact'],
        'tomb_frame': ['exact'],
        'tree': ['exact'],
        'trees': ['exact'],
        'triple_frame': ['exact'],
        'waterfall': ['exact'],
        'waves': ['exact'],
        'windmill': ['exact'],
        'window_frame': ['exact'],
        'winter': ['exact'],
        'wood_framed': ['exact'],
    }
    ordering_fields = [
        'episode'
    ]
    search_fields = [
        'episode'
    ]
