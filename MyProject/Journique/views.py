from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.views import View
from rest_framework import generics, status
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import exception_handler

from .serializers import *
from .forms import *
from .models import Pin, UserProfile, User


def home(request):
    """
    View for the home page displaying pins based on user preferences.
    """
    user = request.user
    if user.is_authenticated:
        user_profile = UserProfile.objects.get_or_create(user=user)[0]
        preferred_categories = user_profile.preferred_categories.all()
        pins = Pin.objects.filter(category__in=preferred_categories, is_deleted=False)
    else:
        # If the user is not authenticated, show all pins
        pins = Pin.objects.filter(is_deleted=False)

    context = {'pins': pins, 'user': user}
    return render(request, 'home.html', context)


def user_list(request):
    """
    View for listing all users.
    """
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})


def user_profile(request, username):
    user = request.user
    user_viewed = get_object_or_404(User, username=username)
    if user == user_viewed:
        return render(request, 'profile.html')

    return render(request, 'user_profile.html', {'user_viewed': user_viewed, 'user': user})


# profile interaction
def is_superuser_request_user(request, user):
    return user.is_superuser or user == request.user


def is_superuser(request, user):
    return user.is_superuser


@login_required
def profile_view(request):
    return render(request, 'profile.html')


class MyPinsView(View):
    """
    View for displaying pins uploaded by the current user.
    """
    template_name = 'my_pins.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user_pins = Pin.objects.filter(user=request.user)
            context = {'user_pins': user_pins}
            return render(request, self.template_name, context)
        else:
            return redirect('login')  # Redirect non-authenticated users to the login page


@login_required
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


@login_required
def delete_profile(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('home')

    return render(request, 'delete_profile.html')


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
    """
    View for selecting preferred categories to view pins only from those
    """
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


def search_results(request):
    """
    view for searching users or categories or pins
    """
    query = request.GET.get('q', '')
    search_type = request.GET.get('search_type', 'pins')

    results = []

    if search_type == 'users':
        results = User.objects.filter(username__icontains=query)
    elif search_type == 'categories':
        results = Category.objects.filter(name__icontains=query)
    elif search_type == 'pins':
        results = Pin.objects.filter(description__icontains=query)

    context = {'results': results, 'query': query, 'search_type': search_type}
    return render(request, 'search_results.html', context)


# pins
def pin_list(request):
    pins = Pin.objects.all()
    return render(request, 'pin_list.html', {'pins': pins})


def pin_detail(request, pin_id):
    """
    view for detailed information about the pin
    """
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

            return redirect('home')
    else:
        form = PinForm()

    return render(request, 'add_pin.html', {'form': form})


def page_not_found_404(request):
    return render(request, '404_error.html')


@login_required
def edit_pin(request, pin_id):
    """
    view for editing a pin (only for the user uploaded the pin and a superuser)
    """
    print(f"Edit Pin view called for pin_id: {pin_id}")

    if not request.user.is_authenticated:
        print("User is not authenticated.")
        return redirect('login')  # Redirect non-authenticated users to the login page

    pin = get_object_or_404(Pin, id=pin_id)

    # Check the rights
    if not (request.user.is_superuser or pin.user == request.user):
        print(f"User {request.user} does not have permission to edit pin {pin_id}")
        return HttpResponseForbidden("You don't have permission to edit this pin.")

    if request.method == 'POST':
        form = PinForm(request.POST, instance=pin)
        if form.is_valid():
            form.save()
            print(f"Pin updated successfully: {pin}")
            return redirect('pin_detail', pin_id=pin.id)
        else:
            print(f"Form errors: {form.errors}")
    else:
        form = PinForm(instance=pin)

    return render(request, 'edit_pin.html', {'form': form, 'pin': pin})


@login_required
def delete_pin(request, pin_id):
    """
        view for deleting s pin (only for the user uploaded the pin and a superuser)
    """
    print(f"delete Pin view called for pin_id: {pin_id}")
    pin = get_object_or_404(Pin, id=pin_id)

    # Check the rights
    if not (request.user.is_superuser or pin.user == request.user):
        print(f"User {request.user} does not have permission to delete pin {pin_id}")
        return HttpResponseForbidden("You don't have permission to delete this pin.")

    if request.method == 'POST':
        pin.delete()
        if request.is_ajax():
            return JsonResponse({'message': 'Pin deleted successfully.'})
        else:
            return redirect('home')

    return render(request, 'delete_pin.html', {'pin': pin})


def category_pins(request, category_id):
    """
    view for displaying pins from a certain category
    """
    category = Category.objects.get(pk=category_id)
    pins = Pin.objects.filter(category=category, is_deleted=False)
    context = {'category': category, 'pins': pins}
    return render(request, 'category_pins.html', context)


# superuser privileges
@user_passes_test(lambda u: u.is_superuser, login_url='home')
def superuser_pin_management(request):
    """
    view for superusers only to manage all the pins
    """
    pins = Pin.objects.all()
    context = {'pins': pins}
    return render(request, 'superuser_pin_management.html', context)


@user_passes_test(lambda u: u.is_superuser, login_url='home')
def superuser_category_management(request):
    """
    view for superusers only to manage all the categories
    """
    categories = Category.objects.all()
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'categories': categories, 'form': form}
    return render(request, 'superuser_category_management.html', context)


@user_passes_test(lambda u: u.is_superuser, login_url='home')
def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoryForm(instance=category)

    return render(request, 'edit_category.html', {'form': form, 'category': category})


@user_passes_test(lambda u: u.is_superuser, login_url='home')
def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    if request.method == 'POST':
        category.delete()
        return redirect('home')

    return render(request, 'delete_category.html', {'category': category})


# DRF
class PinListCreateView(generics.ListCreateAPIView):
    queryset = Pin.objects.all()
    serializer_class = PinSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PinRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pin.objects.all()
    serializer_class = PinSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class UserRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class CategoryRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

