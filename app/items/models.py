from django.db import models
from categorys.models import Category

# Create your models here.
class Item(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField()
  category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

  def __str__(self) :
    return self.title