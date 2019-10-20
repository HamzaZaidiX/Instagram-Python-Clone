from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import newPostForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def well(request):
    # images=Image.objects.all()
    return render(request,'my_insta/index.html')

  
