from django.shortcuts import render, redirect
from .models import Pin
from .forms import PinForm


def home(request):
    return render(request, 'home.html')


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
