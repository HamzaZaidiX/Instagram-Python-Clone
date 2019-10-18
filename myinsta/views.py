from django.shortcuts import render

# Create your views here.
def index():
    images=Image.objects.all()
    return render(request,'my_insta/index.html',{'myinsta':images})
