from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Pin, UserProfile, User
from .forms import PinForm, UserProfileForm
from django.http import HttpResponse
from django.contrib.auth import login as auth_login, authenticate


def home(request):
    return render(request, 'home.html')


def user_list(request): # all users
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})


def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'user_profile.html', {'user': user})


# profile interaction
@login_required
def profile_view(request):
    return render(request, 'profile.html')


@login_required # имба
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserChangeForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserChangeForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)

    return render(request, 'edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
    return render(request, 'login.html')


@login_required
def delete_profile(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('home')

    return render(request, 'delete_profile.html')


def search_users(request):  # search users (need others)
    query = request.GET.get('q')
    results = User.objects.filter(username__icontains=query)
    return render(request, 'search_users.html', {'results': results, 'query': query})


# pins
def pin_list(request):
    pins = Pin.objects.all()
    return render(request, 'pin_list.html', {'pins': pins})


def pin_detail(request, pin_id):
    pin = Pin.objects.get(id=pin_id)
    return render(request, 'pin_detail.html', {'pin': pin})


def add_pin(request):
    if request.method == 'POST':
        form = PinForm(request.POST, request.FILES)

        if form.is_valid():
            pin = form.save(commit=False)
            pin.user = request.user
            pin.save()

            return redirect('pin_list')  # перенаправление после успешного добавления
    else:
        form = PinForm()

    return render(request, 'add_pin.html', {'form': form})


# views
def view_1(request):
    if request.method == 'POST':
        return HttpResponse("View 1 clicked")

def view_2(request):
    if request.method == 'POST':
        return HttpResponse("View 2 clicked")

def view_3(request):
    if request.method == 'POST':
        return HttpResponse("View 3 clicked")

def view_4(request):
    if request.method == 'POST':
        return HttpResponse("View 4 clicked")

def view_5(request):
    if request.method == 'POST':
        return HttpResponse("View 5 clicked")