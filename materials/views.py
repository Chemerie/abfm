from django.shortcuts import render
from products.models import Product, Cart, Slide
from django.core.paginator import Paginator
import json
from django.http import JsonResponse

# Create your views here.

def search_products(request):
	if request.method == 'POST':
		search_str = json.loads(request.body).get('searchText', '')
		products = Product.objects.filter(name__icontains = search_str) | Product.objects.filter(
			initial_price__istartswith = search_str) | Product.objects.filter(
			description__icontains = search_str) | Product.objects.filter(
			category__icontains = search_str) | Product.objects.filter(
			sub_category__icontains = search_str) | Product.objects.filter(
			mode__icontains = search_str) | Product.objects.filter(
			final_price__istartswith = search_str)
		data = products.values()
		return JsonResponse(list(data), safe= False)

def related_products(request):

	if request.method == 'POST':
		search_str = json.loads(request.body).get('searchText')
		product = Product.objects.get(pk=search_str)
		products = Product.objects.filter(sub_category__icontains = product.sub_category) 
		data = products.values()
		return JsonResponse(list(data), safe= False)

		
def home(request):
	if request.user.is_authenticated:
		products = Product.objects.all()
		paginator = Paginator(products, 12)
		page_number = request.GET.get('page')
		slide = Slide.objects.get(pk=1)
		page_obj = Paginator.get_page(paginator, page_number)
		carts = Cart.objects.filter(user=request.user)
		context = {
			'slide':slide,
			'carts': carts,
			'products': products,
			'page_obj': page_obj,
		}
		return render(request, 'materials/home.html', context)
	else:
		products = Product.objects.all()
		slide = Slide.objects.get(pk=1)
		paginator = Paginator(products, 12)
		page_number = request.GET.get('page')
		page_obj = Paginator.get_page(paginator, page_number)
		context = {
			'slide':slide,
			'products': products,
			'page_obj': page_obj,
			}
		return render(request, 'materials/home.html', context)

def samples(request):
	if request.user.is_authenticated:
		products = Product.objects.all()
		carts = Cart.objects.filter(user=request.user)
		context = {
		'carts': carts,
		'products': products,
		}
		return render(request, 'materials/samples.html', context)
	else:
		products = Product.objects.all()
		context = {
		'products': products,
		}
		return render(request, 'materials/samples.html', context)

def product_page(request, id):
	if request.user.is_authenticated:
		products = Product.objects.all()
		product = Product.objects.get(pk=id)
		carts = Cart.objects.filter(user=request.user)
		paginator = Paginator(products, 12)
		page_number = request.GET.get('page')
		page_obj = Paginator.get_page(paginator, page_number)
		context = {
		'carts': carts,
		'product': product,
		'page_obj': page_obj,
		}
		return render(request, 'products/product_page.html', context)
	else:
		products = Product.objects.all()
		product = Product.objects.get(pk=id)

		paginator = Paginator(products, 12)
		page_number = request.GET.get('page')
		page_obj = Paginator.get_page(paginator, page_number)
		context = {
		'product': product,
		'page_obj': page_obj,
		}
		return render(request, 'products/product_page.html', context)

def category_page1(request):
	if request.user.is_authenticated:
		products = Product.objects.filter(category='Material')
		paginator = Paginator(products, 12)
		page_number = request.GET.get('page')
		slide = Slide.objects.get(pk=1)
		page_obj = Paginator.get_page(paginator, page_number)
		carts = Cart.objects.filter(user=request.user)
		context = {
			'cat': 'Material',
			'slide':slide,
			'carts': carts,
			'products': products,
			'page_obj': page_obj,
		}
		return render(request, 'materials/category_page.html', context)
	else:
		products = Product.objects.filter(category='Material')
		slide = Slide.objects.get(pk=1)
		paginator = Paginator(products, 12)
		page_number = request.GET.get('page')
		page_obj = Paginator.get_page(paginator, page_number)
		context = {
			'cat': 'Material',
			'slide':slide,
			'products': products,
			'page_obj': page_obj,
			}
		return render(request, 'materials/category_page.html', context)

def category_page2(request):
	if request.user.is_authenticated:
		products = Product.objects.filter(category='Foam')
		paginator = Paginator(products, 12)
		page_number = request.GET.get('page')
		slide = Slide.objects.get(pk=1)
		page_obj = Paginator.get_page(paginator, page_number)
		carts = Cart.objects.filter(user=request.user)
		context = {
			'cat': 'Foam',
			'slide':slide,
			'carts': carts,
			'products': products,
			'page_obj': page_obj,
		}
		return render(request, 'materials/category_page.html', context)
	else:
		products = Product.objects.filter(category='Foam')
		slide = Slide.objects.get(pk=1)
		paginator = Paginator(products, 12)
		page_number = request.GET.get('page')
		page_obj = Paginator.get_page(paginator, page_number)
		context = {
			'cat': 'Foam',
			'slide':slide,
			'products': products,
			'page_obj': page_obj,
			}
		return render(request, 'materials/category_page.html', context)


def category_page3(request):
	if request.user.is_authenticated:
		products = Product.objects.filter(category='Tool')
		paginator = Paginator(products, 12)
		page_number = request.GET.get('page')
		slide = Slide.objects.get(pk=1)
		page_obj = Paginator.get_page(paginator, page_number)
		carts = Cart.objects.filter(user=request.user)
		context = {
			'cat': 'Tool',
			'slide':slide,
			'carts': carts,
			'products': products,
			'page_obj': page_obj,
		}
		return render(request, 'materials/category_page.html', context)
	else:
		products = Product.objects.filter(category='Tool')
		slide = Slide.objects.get(pk=1)
		paginator = Paginator(products, 12)
		page_number = request.GET.get('page')
		page_obj = Paginator.get_page(paginator, page_number)
		context = {
			'cat': 'Tool',
			'slide':slide,
			'products': products,
			'page_obj': page_obj,
			}
		return render(request, 'materials/category_page.html', context)


def category_page4(request):
	if request.user.is_authenticated:
		products = Product.objects.filter(category='Wood')
		paginator = Paginator(products, 12)
		page_number = request.GET.get('page')
		slide = Slide.objects.get(pk=1)
		page_obj = Paginator.get_page(paginator, page_number)
		carts = Cart.objects.filter(user=request.user)
		context = {
			'cat': 'Wood',
			'slide':slide,
			'carts': carts,
			'products': products,
			'page_obj': page_obj,
		}
		return render(request, 'materials/category_page.html', context)
	else:
		products = Product.objects.filter(category='Wood')
		slide = Slide.objects.get(pk=1)
		paginator = Paginator(products, 12)
		page_number = request.GET.get('page')
		page_obj = Paginator.get_page(paginator, page_number)
		context = {
			'cat': 'Wood',
			'slide':slide,
			'products': products,
			'page_obj': page_obj,
			}
		return render(request, 'materials/category_page.html', context)