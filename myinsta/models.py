from django.db import models

# Create your models here.
class Profile(models.Model):
    photo = models.ImageField(upload_to = 'photos',null=True)
    biography=models.TextField(max_length=60)
     
    def __str__(self):
        return self.profile

class Image(models.Model):
    image=models.ImageField(upload_to = 'pictures',null= True)
    name=models.CharField(max_length=30)
    caption=models.CharField(max_length=30) 
    profile=models.ForeignKey(Profile,null= True)
    comments=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Comments(models.Model):
    comments=models.CharField(max_length=30) 

    def __str__(self):
        return self.comments
       

     
