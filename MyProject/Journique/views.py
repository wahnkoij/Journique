from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from .models import Pin, UserProfile, User


def home(request):
    user = request.user
    if user.is_authenticated:
        user_profile = UserProfile.objects.get_or_create(user=user)[0]
        preferred_categories = user_profile.preferred_categories.all()
        pins = Pin.objects.filter(category__in=preferred_categories, is_deleted=False)
    else:
        # If the user is not authenticated,  show all pins
        pins = Pin.objects.filter(is_deleted=False)

    context = {'pins': pins}
    return render(request, 'home.html', context)


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
            return redirect('select_preferred_categories')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

@login_required
def select_preferred_categories(request):
    if request.method == 'POST':
        form = PreferredCategoriesForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PreferredCategoriesForm(instance=request.user.userprofile)

    context = {'form': form}
    return render(request, 'select_preferred_categories.html', context)

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


@login_required
def add_pin(request):
    if request.method == 'POST':
        form = PinForm(request.POST, request.FILES)

        if form.is_valid():
            pin = form.save(commit=False)
            pin.user = request.user
            pin.save()

            return redirect('pin_list')
    else:
        form = PinForm()

    return render(request, 'add_pin.html', {'form': form})


def page_not_found_404(request):
    return render(request, '404_error.html')


@login_required
def edit_pin(request, pin_id):
    pin = get_object_or_404(Pin, id=pin_id, user=request.user)

    if request.method == 'POST':
        form = PinForm(request.POST, instance=pin)
        if form.is_valid():
            form.save()
            return redirect('pin_detail', pin_id=pin.id)
    else:
        form = PinForm(instance=pin)

    return render(request, 'edit_pin.html', {'form': form, 'pin': pin})


def delete_pin(request, pin_id):
    pin = get_object_or_404(Pin, id=pin_id)

    if request.method == 'POST':
        pin.delete()
        if request.is_ajax():
            return JsonResponse({'message': 'Pin deleted successfully.'})
        else:
            return redirect('home')

    return render(request, 'delete_pin.html', {'pin': pin})


