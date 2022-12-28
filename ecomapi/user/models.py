from django.db import models

# Create your models here.
class usermodel(models.Model):
    #userid=models.BigAutoField()
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    phone=models.CharField(max_length=10)
    email=models.EmailField(max_length=30,primary_key=True)
    def __str__(self):
        return self.email
class useraddressmodel(models.Model):
    #userid=models.ForeignKey(usermodel,on_delete=models.C,unique=True)
    email=models.ForeignKey(usermodel,on_delete=models.CASCADE,unique=True)
    street=models.CharField(max_length=50)
    city=models.CharField(max_length=30)
    dictrict=models.CharField(max_length=30)
    state=models.CharField(max_length=30,default='Tamil Nadu')
    country=models.CharField(max_length=50,default='India')
    def __str__(self):
       #return str(self.userid)+'-'+self.username+' '+self.city
       return str(self.email)