from django.http import HttpResponse
from django.shortcuts import render
from .forms import ImageView
from .models import Image
from  .Rescaling import rescaling
import time
# Create your views here.
def download_image(request):
    if bool(request.FILES):
        p = request.FILES['image']
        form = ImageView(request.POST or None)
        if form.is_valid():
            w=form.cleaned_data['w']
            h=form.cleaned_data['h']
        from .models import Image
        img = Image(image = p,w = w,h = h);
        img.save()
        # time.sleep(3)
        print(rescaling(img.image.name,w,h))
    return render(request,"download.html",{})

def homepage(request, *args, **kwargs):
    w=0
    h=0
    
    
        
        
    return render(request, 'home.html',{})