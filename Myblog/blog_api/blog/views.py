from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from blog.serializers import BlogSerializer
from .models import Blog
# Create your views here.

class Test_end_point(APIView):
    def get(self, request,id=None):
        
        if id:
            try:
                query = Blog.objects.get(id=id)
                serializer = BlogSerializer(query, many=False)
                return Response(serializer.data)
            except Blog.DoesNotExist:
                return Response({'Message':"The blog doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
        
        queryset = Blog.objects.all()
        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = BlogSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response()
    
    def put(self,request,id):

        query = Blog.objects.get(id=id)
        serializer = BlogSerializer(instance=query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    def delete(self, request, id):
        query = Blog.objects.get(id=id)
        query.delete()
        return Response('Data successfully deleted!')