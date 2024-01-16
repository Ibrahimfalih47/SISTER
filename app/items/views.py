from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Item
from categorys.models import Category
from rest_framework import status
from .serializers import ItemSerializer

class ItemListView(APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            # Ambil ID kategori dari data permintaan
            category_id = request.data.get('category', None)

            # Periksa apakah kategori dengan ID yang diberikan ada
            try:
                category = Category.objects.get(id=category_id)
            except Category.DoesNotExist:
                return Response({'error': 'Category not found'}, status=status.HTTP_400_BAD_REQUEST)

            item = serializer.save(category=category)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemDetailView(APIView):
    def get_object (self, pk):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return None
     
    def get(self, request, pk):
        item = self.get_object(pk)
        if item :
            serializer = ItemSerializer(item)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)
   
    def put(self, request, pk):
        item = self.get_object(pk)
        if item :
            serializer = ItemSerializer(item, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk):
        item = self.get_object(pk)
        if item :
            item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT, data={"message": "Item Deleted Successfully"})
        return Response(status=status.HTTP_404_NOT_FOUND)