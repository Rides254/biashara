from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Member
from bizzapp.forms import ProductForm
from bizzapp.models import Product


# Create your views here.
def register(request):
    if request.method == 'POST':
        member = Member(firstname=request.POST['firstname'], lastname=request.POST['lastname'],
                        username=request.POST['username'], password=request.POST['password'])
        member.save()
        return redirect('/')
    else:
        return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def index(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            member = Member.objects.get(username=request.POST['username'], password=request.POST['password'])
            return render(request, 'index.html', {'member': member})
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def about(request):
    return render(request, 'about.html')


def appointment(request):
    return render(request, 'appointment.html')


def add(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    else:
        form = ProductForm()
        return render(request, "addproducts.html", {'form': form})


def show(request):
    products = Product.objects.all()
    return render(request, 'show.html', {'products': products})

def delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('/show')

def edit(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'edit.html', {'product': product})


def update(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST, instance=product)
    if form.is_valid():
        form.save()
        return redirect('/show')
    else:
        return render(request, 'edit.html', {'product': product})

