from django.shortcuts import render, redirect 
from django.http import HttpResponse 
from .forms import *
# Create your views here.

def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = Form(request.POST, request.FILES)
        if form.is_valid(): 
            form.save()
            img_obj = form.instance
            Posts = Post.objects.all()      
            return render(request, 'app/viewPhotos.html', {'posts' : Posts, 'full': True})
    else:
        form = Form()
    return render(request, 'app/index.html', {'form': form})

def viewPhotos(request):
    Posts = Post.objects.all()  
    return render(request, 'app/viewPhotos.html', {'posts' : Posts, 'full': True})