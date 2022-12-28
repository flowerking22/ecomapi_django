from django.db import models
from user.models import usermodel
from product.models import productmodel
# Create your models here.
class ordersmodel(models.Model):
    email=models.ForeignKey(usermodel,on_delete=models.CASCADE)
    productname=models.ForeignKey(productmodel,on_delete=models.CASCADE)
    quantity=models.IntegerField(max_length=3,default=1)
    date=models.DateField(auto_now_add=True)
    delevery_status=models.BooleanField(default=False)
    def __str__(self):
        return str(self.email)