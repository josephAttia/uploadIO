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
    return render(request, 'app/viewPhotos.html', {'posts' : Posts, 'full': True})

def edit(request, name):
    if request.method == "POST":
        newName = request.POST['name']
        form = request.GET.get('name', newName)
        Posts = Post.objects.all()
        Posts.filter(name = name).update(name=form)
        return render(request, 'app/viewPhotos.html', {'posts': Posts})
    return render(request, 'app/edit.html', {'name': name})