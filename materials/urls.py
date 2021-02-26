from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
	path('', home, name='home'),
	path('samples', samples, name="samples"),
	path('<int:id>', product_page, name="product_page"),
	path('search_products', csrf_exempt(search_products), name="search_products"),
	path('related_products', csrf_exempt(related_products), name="related_products"),
	path('category_page1', csrf_exempt(category_page1), name="category_page1"),
	path('category_page2', csrf_exempt(category_page2), name="category_page2"),
	path('category_page3', csrf_exempt(category_page3), name="category_page3"),
	path('category_page4', csrf_exempt(category_page4), name="category_page4"),

]