from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from .models import Super


   # supers = Super.objects.all()
@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET':

        super_type_name =request.query_params.get('super_type')
        print(super_type_name)

        queryset = Super.objects.all()
        
        if super_type_name:
            queryset = queryset.filter(super_type__name=super_type_name)

        serializer = SuperSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      

@api_view(['GET', 'PUT', 'DELETE'])
def super_detail(request, pk):
    super = get_object_or_404(Super, pk=pk) 
    if request.method == 'GET':
       serializer = SuperSerializer(super);
       return Response(serializer.data)
    elif request.method == 'PUT':
       serializer = SuperSerializer(super, data=request.data)
       serializer.is_valid(raise_exception=True)
       serializer.save()
       return Response(serializer.data)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
   
@api_view(['GET'])
def custom_response(request):
    if request.method == 'GET':
        heroes = Super.objects.filter(super_type_id=1)
        villians = Super.objects.filter(super_type_id=2)
        hero_serializer = SuperSerializer(heroes, many=True)
        villian_serializer = SuperSerializer(villians, many=True)
        custom_response = {
            "heroes": hero_serializer.data,
            "villians": villian_serializer.data
        }
        return Response(custom_response,status=status.HTTP_200_OK)