from django.shortcuts import render
from .forms import myForm

# Create your views here.
def well(request):
    # images=Image.objects.all()
    if request.method == 'POST':
        form = myForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form = myForm()
    return render(request,'my_insta/index.html',{"letterForm":form})
