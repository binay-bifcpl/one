from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404, redirect
from .models import Requisition
from .forms import RequisitionForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with the URL name of your home page
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')  # Replace 'login.html' with the path to your login template

@login_required(login_url='login')  # Replace 'login' with the URL name of your login page
def home_view(request):
    return render(request, 'home.html')  # Replace 'home.html' with the path to your home template

@login_required(login_url='login')  # Replace 'login' with the URL name of your login page
def create_requisition(request):
    if request.method == 'POST':
        name = request.POST['name']
        quantity = request.POST['quantity']
        date = request.POST['date']
        image = request.FILES['image']
        user = request.user

        requisition = Requisition.objects.create(
            name=name,
            quantity=quantity,
            date=date,
            image=image,
            user=user
        )
        return redirect('home')  # Replace 'home' with the URL name of your home page

    return render(request, 'home.html')

@login_required(login_url='login')  # Replace 'login' with the URL name of your login page
def requisition_list(request):
    user = request.user
    requisitions = Requisition.objects.filter(user=user)

    return render(request, 'requisition_list.html', {'requisitions': requisitions})

def logout_view(request):
    logout(request)
    return redirect('index') # or render a template

def index(request):
    return render(request, 'index.html')

def edit_requisition(request, pk):
    requisitions = get_object_or_404(Requisition, pk=pk, user=request.user)
    if request.method == 'POST':
        form = RequisitionForm(request.POST, request.FILES, instance=requisitions)
        if form.is_valid():
            form.save()
            return redirect('requisition_list')
    else:
        form = RequisitionForm(instance=requisitions)
    return render(request, 'edit_requisition.html', {'form': form})

def delete_requisition(request, pk):
    requisition = get_object_or_404(Requisition, pk=pk, user=request.user)
    if request.method == 'POST':
        requisition.delete()
        return redirect('requisition_list')
    return render(request, 'delete_requisition.html', {'requisition': requisition})
