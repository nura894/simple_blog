from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    title     = models.CharField(max_length=255, blank=False, null=False)
    created_at= models.DateTimeField(auto_now_add=True)
     

    def clean(self):
      if not self.title:
          raise ValidationError('Title cannot be empty.')

    def __str__(self):
      return self.title


class Course(models.Model):
    title      = models.CharField(max_length=255, blank=False, null=False)
    price      = models.FloatField(blank=False, null=False)
    student_qty= models.IntegerField( blank=False, null=False) 
    reviews_qty= models.IntegerField(blank=False, null=False)
    category   = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='coursa')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='courses')



    @property
    def price_morethan_zero(self) -> bool:
        return self.price > 0


    def clean(self):  #full_clean() method calls this clean() method
      if self.price is not None and self.price <= 0:
          raise ValidationError({'price': "Price cannot be negative."})
      if self.student_qty is not None and self.student_qty <= 0:
          raise ValidationError({'student_qty': "Student Qty cannot be negative."})
      if self.reviews_qty is not None and self.reviews_qty <= 0:
          raise ValidationError({'reviews_qty': "Reviews Qty cannot be negative."})
    
     
    def __str__(self):
      return self.title