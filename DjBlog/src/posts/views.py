from django.shortcuts import render ,redirect
from .forms import postForm

from .models import post
# Create your views here.
def post_list (request):
    data = post.objects.all()
    print(data)
    return render(request,'posts.html',{'posts':data})
    
    

def post_detail(request,id_post):
    data = post.objects.get(id=id_post)
    return render(request,'datail.html',{'post':data})


def new_post(request):
    if request.method == 'POST':
        form = postForm(request.POST,request.FILES)
        if form .is_valid():
            form.save()
            return redirect('/blog/')

    else:

     
        form = postForm()
    return render (request,'new.html',{'form':form})

def edit_post(request,id_post):
    data = post.objects.get(id=id_post)
    if request.method == 'POST':
        form = postForm(request.POST,request.FILES,instance=data)
        if form .is_valid():
            form.save()
            return redirect('/blog/')

    else:

     
        form = postForm(instance=data)
    return render (request,'edit.html',{'form':form})


   
    