from django.shortcuts import render, redirect
from .models import Product, Cart, Slide
from django.contrib import messages 
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse

# Create your views here.


def add_product(request):
	if request.method == 'POST':
		name = request.POST['product_name']
		category = request.POST['category']
		mode = request.POST['mode']
		sub_category = request.POST.get('sub-category')
		description = request.POST['description']
		initial_price = request.POST['initial_price']
		final_price = request.POST['current_price']
		original_pics = request.FILES.get('original_picture')
		pics1 = request.FILES.get('pic1')
		pics2 = request.FILES.get('pic2')
		pics3 = request.FILES.get('pic3')


		product = Product(name=name, category=category,mode=mode, sub_category=sub_category,  description=description, initial_price=initial_price, final_price=final_price, original_pics=original_pics, pics1=pics1, pics2=pics2, pics3=pics3)
		product.save()
		messages.success(request, 'Product saved successfully')
		return render(request, 'products/add_product.html')

	return render(request, 'products/add_product.html')





def edit_product(request, id):
	product = Product.objects.get(pk=id)
	if request.method == 'POST':
		name = request.POST['product_name']
		category = request.POST['category']
		mode = request.POST['mode']
		sub_category = request.POST.get('sub-category')
		description = request.POST['description']
		initial_price = request.POST['initial_price']
		final_price = request.POST['current_price']
		original_pics = request.FILES.get('original_picture')
		pics1 = request.FILES.get('pic1')
		pics2 = request.FILES.get('pic2')
		pics3 = request.FILES.get('pic3')


		product.name = name
		product.category = category
		product.sub_category = sub_category
		product.mode = mode
		product.description = description
		product.initial_price = initial_price
		product.final_price = final_price
		product.original_pics = original_pics
		product.pics1 = pics1
		product.pics2 = pics2
		product.pics3 = pics3

		product.save()
		messages.success(request, 'Product updated successfully')
		return redirect('home')



	context = {
	'product': product,
	'values': product,
	}

	return render(request, 'products/edit_product.html', context)



def delete_product(request, id):
	product = Product.objects.get(pk=id)
	product.delete()
	messages.success(request, 'Expense deleted succesfully')
	return redirect('home')


# @login_required(login_url='products/closed')
def add_cart(request, id):
	product = Product.objects.get(pk=id)
	chec = Cart.objects.filter(product=product, user=request.user).exists()
	if chec:
		# messages.success(request, 'Product added to the cart')
		return JsonResponse({'message_error': 'Product already in the cart'}, status=400)

    		
	else:
		cart = Cart()
		cart.product = product
		cart.user = request.user
		cart.save()
		# messages.success(request, 'Product added to the cart')
		# return redirect('home')
		return JsonResponse({'message_success': 'Product Added to Cart'})
	

		# if not str(username).isalnum():
		# 	return JsonResponse({'username_error_message': 'The username most be an alpha numeric number'}, status=400)


		# if User.objects.filter(username=username).exists():
		# 	return JsonResponse({'username_error_message': 'Sorry username is used, chose another one'}, status=409)

		# return JsonResponse({'username_validate': True})
					
 

def cart(request):
	if request.user.is_authenticated:
		carts = Cart.objects.filter(user=request.user)

		context = {
		'carts': carts,
		}
		return render(request, 'products/cart.html', context)
	else:
		return render(request, 'products/cart.html', context)

def closed(request):
	return render(request, 'products/closed.html')



def edit_slide(request):
	slide = Slide.objects.get(pk=1)
	if request.method == 'POST':
		slide.slide1heading = request.POST['slide1heading']
		slide.slide2heading = request.POST['slide2heading']
		slide.slide3heading = request.POST['slide3heading']
		slide.slide4heading = request.POST['slide4heading']

		slide.slide1subheading = request.POST['slide1subheading']
		slide.slide2subheading = request.POST['slide2subheading']
		slide.slide3subheading = request.POST['slide3subheading']
		slide.slide4subheading = request.POST['slide4subheading']

		slide.slide1writeup = request.POST['slide1writeup']
		slide.slide2writeup = request.POST['slide2writeup']
		slide.slide3writeup = request.POST['slide3writeup']
		slide.slide4writeup = request.POST['slide4writeup']

		slide.slide1pics = request.FILES.get('slide1pics')
		slide.slide2pics = request.FILES.get('slide2pics')
		slide.slide3pics = request.FILES.get('slide3pics')
		slide.slide4pics = request.FILES.get('slide4pics')

	
		slide.save()
		context = {
			'value': slide,
		}
		messages.success(request, 'Product updated successfully')
		return render(request, 'products/edit_slide.html', context)



	context = {
	'value': slide,
	}

	return render(request, 'products/edit_slide.html', context)


