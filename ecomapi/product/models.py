from django.db import models

# Create your models here.
def file_directory_path(instance, filename):
    return f"productimage/{filename}"

class productmodel(models.Model):
    #productid=models.IntegerField(default=0)
    name=models.CharField(max_length=50,primary_key=True)
    price=models.IntegerField(max_length=10)
    category=models.CharField(max_length=30)
    img=models.ImageField(upload_to=file_directory_path)
    spec1=models.CharField(max_length=50)
    spec2=models.CharField(max_length=50)
    line1=models.CharField(max_length=50)
    line2=models.CharField(max_length=50)
    line3=models.CharField(max_length=50)
    line4=models.CharField(max_length=50)
    def __str__(self):
        return self.name