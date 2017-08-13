from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.utils import timezone

from .forms import SignUpForm,PostForm,SignupNextForm
from .models import Post,Profile



# Create your views here.
def post(request):
    return render(request,'posts/home.html')

def list_view(request):
    queryset = Post.objects.all()
    context = {
        "title": "List",
        "brief": "List",
        "posts": queryset,
    }
    return render(request,'posts/index.html',context)

def profile(request):
    return render(request,'posts/profile.html')

def blog(request):
    return render(request,'posts/blog.html')

#def edit(request):
    #return render(request,'posts/extra.html')

def edited(request):
    return render(request,'posts/edit.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user_profile = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('next')
    else:
        form = SignUpForm(request.POST or None)
        form1 = SignupNextForm(request.POST or None)
    return render(request, 'posts/signup.html', {'form': form})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post_obj = form.save()
            post_obj.save()
            return redirect('home')
    else:
        form = PostForm(request.POST or None)
    return render(request, 'posts/edit.html', {'form': form})

def new(request):
    if request.method == 'POST':
        form = SignupNextForm(request.POST)
        if form.is_valid():
            post_obj = form.save()
            post_obj.user = request.user
            post_obj.save()
            return redirect('profile')
    else:
        form = SignupNextForm(request.POST or None)
    return render(request,'posts/post_form.html', {'form': form})






