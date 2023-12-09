from django.shortcuts import render, redirect
from .models import Pin, UserProfile, User
from .forms import PinForm
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def profile_view(request):
    user = UserProfile.user
    image = UserProfile.image
    bio = UserProfile.bio
    return render(request, 'profile.html')


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


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.get(username=username)
        if user.check_password(password):
            request.session['user_id'] = user.id
            return redirect('home')
    return render(request, 'login.html')

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
