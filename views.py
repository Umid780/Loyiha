from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def index(request):
    query = request.GET.get('q')
    region = request.GET.get('region')
    products = Product.objects.all()
    if query:
        products = products.filter(name__icontains=query)
    if region:
        products = products.filter(region=region)
    return render(request, 'index.html', {'products': products})

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('/')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})
