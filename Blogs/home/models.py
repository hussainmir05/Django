from django.db import models

# Create your models here.
class Blog(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    slug=models.CharField(max_length=100)
    content=models.TextField(max_length=10000)
    time= models.DateTimeField (auto_now_add=True)
    
    def __str__(self):
        return self.title 
class Contect(models.Model):
    sno=models.AutoField(primary_key=True)

    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    passwd=models.CharField(max_length=200)
    desc=models.TextField()
    time=models.DateTimeField(auto_now_add=True)
     
    def __str__(self):
        contex=[self.name, self.email]
        return self.name
       