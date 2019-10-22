from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    photo = models.ImageField(upload_to = 'photos',null=True)
    biography=models.TextField(max_length=60)
    def __str__(self):
        return self.biography

class Image(models.Model):
    image=models.ImageField(upload_to = 'pictures',null= True)
    name=models.CharField(max_length=30)
    caption=models.CharField(max_length=30) 
    post = HTMLField()
    profile=models.ForeignKey(Profile,null= True)
    user=models.ForeignKey(User,blank=True,null=True)
    comments=models.CharField(max_length=30)


    def __str__(self):
        return self.name
    
    def save_image(self):
        return self.save() 
    
    def update_image(self):
        return self.update() 

    def delete_image(self):
        return self.delete() 


class Comments(models.Model):
    comments=models.CharField(max_length=30)
    # commented_image = models.ForeignKey('Image',on_delete=models.CASCADE) 

    def __str__(self):
        return self.comments
       

      

     
