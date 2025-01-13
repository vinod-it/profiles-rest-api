from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers



class HelloApiView(APIView):
    """Test API view"""
    serializer_class = serializers.HelloSerializer

    def get(self, response,format=None):
        """Return a list[] of APIView features"""
        an_apiview = ['Uses HTTP methods as function (get,post,patch, put, delete)',
        'Is similar to a traditional Django view',
        'Gives you the most control over the application logic',
        'Is mapped manually to URLs'
        ]

        return Response({'message':'Hello..','an_apiview': an_apiview})

    def post(self,request):
        """create a hello msg with our name"""
        serializer = self.serializer_class(data = request.data)

        if(serializer.is_valid()):
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"
            return Response ({'message':message})
        else :
            return Response (serializer.errors,
            status = status.HTTP_400_BAD_REQUEST

            )

    def put(self, request , pk = None): # pk takes the objects id which is going to be updating
        """Handle updating an object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an objects"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Return a hello massage"""
    serializer_class = serializers.HelloSerializer

    def list(self,request):
        a_viewset = [
        'Uses action (list,create, retrieve, update, partial_update)',
        'Automatically maps to URLs  using Routers',
        'Provides more functionality with less code',
        ]

        return Response({'message':'Hello','a_viewset':a_viewset})


    def create(self, request):
        """create a new hello massage"""
        serializer = self.serializer_class(data = request.data)

        if(serializer.is_valid()):
            name = serializer.validated_data.get('name')
            message = f"Hello, {name}!!"
            return Response({'message':message})
        else : return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'Http_method':'GET'})

    def update(self, request, pk = None):
        """Handle updating an object"""
        return Response({'Http_method':'PUT'})

    def partial_update(self, request, pk = None):
        """Handle updating part of an object"""
        return Response({'Http_method':'PATCH'})

    def destroy(self, request, pk = None):
        """Handle removing an object"""
        return Response({'Http_method':'DELETE'})   
