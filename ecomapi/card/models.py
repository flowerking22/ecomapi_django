from django.db import models
# Create your models here.
from product.models import productmodel
from user.models import usermodel
# Create your models here.
class cardmodel(models.Model):
    email=models.ForeignKey(usermodel,on_delete=models.CASCADE)
    productname=models.ForeignKey(productmodel,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    quantity=models.IntegerField(default=1)
    def __str__(self):
        return str(self.email)+''+str(self.productname)