from rest_framework import serializers
from .models import Item
from reviews.serializer import ReviewSerializer
from categorys.serializers import CategorySerializer

class ItemSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    # category = CategorySerializer(many=True, read_only=True)
    class Meta:
        model = Item
        fields = ['id', 'title', 'description', 'reviews', 'category']