from django.shortcuts import render
from toyapp.models import  Product
from django.db.models import Q




def searchResult(requset):
    products=None
    query=None
    if 'q' in requset.GET:
        query=requset.GET.get('q')
        products=Product.objects.all().filter(Q(name__contains=query)| Q(description__contains=query))
    return render(requset,'search.html',{'query':query,'products':products})

