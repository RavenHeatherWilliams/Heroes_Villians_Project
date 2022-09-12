from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from .models import Super



@api_view(['GET', 'POST'])
def supers_list(request):
    
    if request.method == 'GET':

        supers = Super.objects.all()

        serializer = SuperSerializer(supers, many=True)
    
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        if serializer.is_valid() == True:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def super_detail(request, pk):

    print(pk)
    return Response(pk)