from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.
def index(request):
	# product_list=Product.objects.all()
	
	# parameter={'num_of_slides':num_of_slides, 'range': range(1,num_of_slides)  ,'product_list':product_list}
	# all_product=[[product_list, range(1, num_of_slides), num_of_slides],
	# 			[product_list, range(1, num_of_slides), num_of_slides]]
	all_product=[]
	category=Product.objects.values('category', 'id')
	cats ={item['category'] for item in category}
	for cat in cats:
		prod=Product.objects.filter(category=cat)
		n=len(prod)
		num_of_slides=n//4+ceil((n/4)-(n//4))
		all_product.append([prod, range(1, num_of_slides), num_of_slides])
	parameter={'all_product':all_product}
	return render(request, "shop/index.html", parameter)

def about(request):
	return render(request, "shop/about.html")

def contact(request):
	return render(request, "shop/index.html")

def tracker(request):
	return render(request, "shop/index.html")

def search(request):
	return render(request, "shop/index.html")

def productview(request):
	return render(request, "shop/index.html")

def checkout(request):
	return render(request, "shop/index.html")