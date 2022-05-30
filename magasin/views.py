
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from magasin.models import Product

def index(request):
    products=Product.objects.all()
    return render(request,"magasin/index.html",context={"products":products})
def product_detail(request,slug):
    product=get_object_or_404(Product,slug=slug)
    return 
