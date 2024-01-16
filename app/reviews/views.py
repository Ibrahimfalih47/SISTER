from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from items.models import Item
from .models import Review
from .serializer import ReviewSerializer  # Sesuaikan dengan nama file serializer yang benar

class ReviewView(APIView):
    def get(self, request):
        review = Review.objects.all()
        serialize = ReviewSerializer(review, many=True)
        return Response(serialize.data)

    def post(self, request, item_id):
        try:
            item = Item.objects.get(pk=item_id)
        except Item.DoesNotExist:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(item=item)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DetailReview(APIView):
    def get_object(self, pk):
        try:
            return Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            return None
    
    def get(self, request, pk):
        review = self.get_object(pk)
        if review:
            serialize = ReviewSerializer(review)
            return Response(serialize.data)
        return Response(status=status.HTTP_404_NOT_FOUND)
   
    def put(self, request, pk):
        review = self.get_object(pk)
        if review :
            serializer = ReviewSerializer(review, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk):
        review = self.get_object(pk)
        if review :
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT, data={"message": "Item Deleted Successfully"})
        return Response(status=status.HTTP_404_NOT_FOUND)
    