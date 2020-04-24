from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework import status

class UserAPI(APIView): #vista basada en clase 
  def post(self,request):
    serializer = UserSerializer(data = request.data) #en rest toca llmar request.data para obtener los datos
    if serializer.is_valid():
      user= serializer.save()
      message= f'Hello {user}'
      return Response(message, status= status.HTTP_201_CREATED ) 
    else:
      return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST ) 
  
  def get(self, request):
    return Response({'message': 'hello'})
  
  def put(self,request,pk=None):
    """Handle updating an object"""
    return Response({'method': 'PUT'})
  
  def patch(self,request,pk=None):
    """Handle a partial update of an object"""
    return Response({'method': 'PATCH'})

  def delete(self,request,pk=None):
    """Delete an object"""
    return Response({'method': 'DELETE'})

