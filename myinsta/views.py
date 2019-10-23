from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import newPostForm,ProfileForm
from .models import Image,Profile,User
from django.http import HttpResponse

# Create your views here.
@login_required(login_url='/accounts/login/')
def welc(request):
    current_user=request.user
    pic_images=Image.objects.all()
    profile=Profile.objects.filter(user=current_user).first()
    return render(request,'my_insta/index.html',{"pic_images":pic_images,"profile":profile})


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
def profile(request):
    current_user = request.user
    profile=Profile.objects.filter(user=current_user).first()
    print(profile)
    images=Image.objects.filter(user=current_user)
    return render(request, 'my_insta/new_profile.html', {"images":images,"profile":profile})
  
def new_post(request):
    current_user = request.user
    profile=Profile.objects.filter(user=current_user).first
    if request.method == 'POST':
        form = newPostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.Profile=profile
            image.save()
        return redirect('well')

    else:
        form = newPostForm()
    return render(request, 'new_post.html', {"form": form})

def search_results(request):

    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        searched_photos = Image.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'my_insta/search.html',{"message":message,"photos": searched_photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'my_insta/search.html',{"message":message})    

