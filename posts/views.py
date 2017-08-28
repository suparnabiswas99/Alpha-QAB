from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages

from .forms import SignUpForm,PostForm, ProfileForm
from .models import Post,Profile

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def post(request):
    return render(request,'posts/home.html')

def list_view(request):
    queryset_list = Post.objects.all()

    paginator = Paginator(queryset_list, 5)  # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "title": "List",
        "brief": "List",
        "posts": queryset,
        "page_request_var": page_request_var,
    }

    return render(request,'posts/index.html',context)



def profile(request):
    obj = Profile.objects.get(user = request.user)
    return render(request,'posts/profile.html',{'object': obj})

def blog(request, id=None):
    instance = Post.objects.get(id=id)
    context = {
        "title": instance.title,
        "instance": instance,
    }
    return render(request,'posts/blog.html', context)


def edited(request):
    return render(request,'posts/edit.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('createprofile')
    else:
        form = SignUpForm()
    return render(request, 'posts/signup.html', {'form': form})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post_obj = form.save()
            post_obj.save()
            # message success
            messages.success(request, "Successfully Created")
            return redirect('index')
    else:
        form = PostForm(request.POST or None)
        messages.error(request, "Not Successfully Created")

    return render(request, 'posts/edit.html', {'form': form})


def post_update(request, id=None):
    instance = Post.objects.get(id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #message success
        messages.success(request, "Successfully Edited")
        return redirect('index')
    context = {
        "title": instance.title,
        "instance": instance,
        "form":form,
    }
    return render(request, "posts/edit1.html", context)

def post_delete(request, id=None):
    instance = Post.objects.get(id=id)
    instance.delete()
    messages.warning(request, "Successfully deleted")
    return redirect("index")

def Profile_Update(request):
    if Profile.objects.filter(user = request.user).exists():
        instance = Profile.objects.get(user = request.user)
        form = ProfileForm(request.POST or None, request.FILES or None,instance=instance)
        if form.is_valid():
            profile_obj = form.save(commit=False)
            profile_obj.save()
            return redirect('profile')
        context = {
            "instance": instance,
            "form": form,
        }
        return render(request,"posts/post_form.html",context)

    else:
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES or None)
            if form.is_valid():
                profile_obj = form.save(commit=False)
                profile_obj.user = request.user
                profile_obj.save()
                return redirect('profile')
        else:
            form = ProfileForm(request.POST or None)
        return render(request, 'posts/post_form.html', {'form': form})