from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .form import ProfileUpdateForm, UserRegisterForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Sonnet

# Create your views here.
@login_required(login_url='/login/')
def home(request):
    return render(request,'base.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})    

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                  request.FILES,
                                  instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')

            return redirect('profile')
    
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)
@login_required
def post_index(request):
    posts = Sonnet.objects.all().order_by('-created')
    context = {
        'posts' : posts
    }
    return render(request, "home.html", context)

#def poem_detail(request, pk)
@login_required
def my_posts(request):
    current_user = request.user
    posts = Sonnet.objects.filter(owner=current_user)
    context = {
        'posts' : posts
    }
    return render(request, 'mypoems.html', context)


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("login")
