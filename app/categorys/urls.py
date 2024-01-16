from django.urls import path
from .views import CategoryList, CategoryDetil

urlpatterns = [
  path("categorys", CategoryList.as_view(), name='list-categorys'),
  path("categorys/<int:pk>", CategoryDetil.as_view(), name='detail-categorys'),
  # path('items/<int:item_id>/reviews', ReviewView.as_view(), name='detail-item'),
]