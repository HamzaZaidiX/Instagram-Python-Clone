from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import newPostForm,ProfileForm
from .models import Image,Profile
from django.http import HttpResponse

# Create your views here.
@login_required(login_url='/accounts/login/')
def welc(request):
    pic_images=Image.objects.all()
    return render(request,'my_insta/index.html',{"pic_images":pic_images})


def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = newPostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('well')

    else:
        form = newPostForm()
    return render(request, 'new_post.html', {"form": form})

@login_required(login_url='/accounts/login/')
def profile_form(request):
   current_user = request.user
   if request.method == 'POST':
       form = ProfileForm(request.POST, request.FILES)
       if form.is_valid():
           profile = form.save(commit=False)
           profile.user = current_user
           profile.save()
       return redirect('profile')
   else:
       form = ProfileForm()
   return render(request, 'my_insta/profile.html', {"form": form})


@login_required(login_url='/accounts/login/')
def profile(request,username=None):
   current_user = request.user
   if not username:
       username=request.user.username
       images=Profile.objects.filter(photo=username).first()
   return render(request, 'my_insta/new_profile.html', {"profile": images,"current_user":current_user})
  
