from django.urls import path
from .views import *


urlpatterns = [
	path('add-product', add_product, name="add_product"),
	
	path('edit-product/<int:id>', edit_product, name="edit_product"),
	path('delete-product/<int:id>', delete_product, name="delete_product"),
	path('add_cart/<int:id>', add_cart, name="add_cart"),
	path('cart', cart, name="cart"),
	path('closed', closed, name="closed"),
	path('edit_slide', edit_slide, name="edit_slide"),
	
	

]