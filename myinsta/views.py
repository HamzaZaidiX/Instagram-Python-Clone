from django.shortcuts import render

# Create your views here.
def well(request):
    # images=Image.objects.all()
    return render(request,'my_insta/index.html')
