from django.db import models
from items.models import Item

# Create your models here.
class Review(models.Model):
  item = models.ForeignKey(Item, related_name='reviews', on_delete=models.CASCADE)
  ratting = models.IntegerField()
  body = models.TextField()

  def __str__(self):
        return f"Review for {self.item.title}"