from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import newPostForm

# Create your views here.
def well(request):
    # images=Image.objects.all()
    return render(request,'my_insta/index.html')

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = newPostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('/')

    else:
        form = newPostForm()
    return render(request, 'new_post.html', {"form": form})    
