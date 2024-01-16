from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import  Category
from .serializers import  CategorySerializer

class CategoryList(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetil(APIView):
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return None
   
    def get(self, request, pk):
        category = self.get_object(pk)
        if category :
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)
   
    def put(self, request, pk):
        category = self.get_object(pk)
        if category :
            serializer = CategorySerializer(category, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    def delete(self, request, pk):
        review = self.get_object(pk)
        if review :
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT, data={"message": "Review Deleted Successfully"})
        return Response(status=status.HTTP_404_NOT_FOUND)