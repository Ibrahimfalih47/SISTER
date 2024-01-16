from django.urls import path
from .views import ItemListView, ItemDetailView

urlpatterns = [
  path('items', ItemListView.as_view(), name='list-item'),
  path('items/<int:pk>', ItemDetailView.as_view(), name='detail-item')
]