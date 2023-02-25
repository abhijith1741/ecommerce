from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,InvalidPage
# Create your views here.
def home(request,c_slug=None):
    # else:
    #     prodt=Products.objects.all()
    cat=Category.objects.all()
    return render(request,'index.html',{'ct':cat})

def products(request,c_slug=None):
    c_page=None
    prodt=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        prodt=Products.objects.filter(category=c_page,available=True)
    paginator=Paginator(prodt,2)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        pro=paginator.page(page)
    except(EmptyPage,InvalidPage):
        pro=paginator.page(paginator.num_pages)
    return render(request,'details.html',{"prodt":prodt,"c_name":c_page,"pg":pro})

def prodDetails(request,c_slug,prod_slug):
    prod=Products.objects.get(category__slug=c_slug,slug=prod_slug)
    return render(request,'products.html',{'prod':prod})

def search(request):
    if request.method=='POST':
        query=request.POST['search']
        prod=Products.objects.all().filter(Q(name__contains=query) | Q(desc__contains=query))
    return render(request,'search.html',{'prod':prod})