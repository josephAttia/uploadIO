from django.shortcuts import render, redirect 
from django.http import HttpResponse 
from .forms import *
# Create your views here.

def image_upload_view(request):
    if request.method == 'POST':
        form = Form(request.POST, request.FILES)
        if form.is_valid(): 
            form.save()
            img_obj = form.instance
            Posts = Post.objects.all()      
            print(Posts)
            return redirect('/view', {'posts': Posts})
    else:
        form = Form()
    return render(request, 'app/index.html', {'form': form})

def viewPhotos(request):
    Posts = Post.objects.all()  
    return render(request, 'app/viewPhotos.html', {'posts' : Posts})

def edit(request, name):
    if request.method == "POST":
        # Requesting Data
        form = Form(request.POST, request.FILES)
        # Data Analyzing 
        if form.is_valid():
            Posts = Post.objects.all()
            data = Posts.get(name=name)
            data.delete()
            form.save()
            return redirect('/view', {'posts': Posts})
    else:
        form = Form()
    return render(request, 'app/edit.html', {'name': name, 'form': form})
