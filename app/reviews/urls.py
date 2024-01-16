from django.urls import path
from .views import ReviewView, DetailReview

urlpatterns = [
  path("reviews", ReviewView.as_view(), name='list-review'),
  path("reviews/<int:pk>", DetailReview.as_view(), name='detail-review'),
  path('items/<int:item_id>/reviews', ReviewView.as_view(), name='detail-item'),
]