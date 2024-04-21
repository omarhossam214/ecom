from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse, HttpResponseBadRequest

def cart_summary(request):
    # get the cart
    cart = Cart(request)
    cart_products = cart.get_products
    quantities = cart.get_quants

    return render(request, 'cart_summary.html', {"cart_products":cart_products, "quantities":quantities})

def cart_add(request):
    # get the cart
    cart = Cart(request)

    if request.method == 'POST' and request.POST.get('action') == 'post':
        product_id_str = request.POST.get('product_id')
        product_qty = int(request.POST.get('product_qty'))
        
        # Check if 'product_id_str' is provided and not empty
        if product_id_str:
            try:
                # Convert 'product_id_str' to an integer
                product_id = int(product_id_str)
                # lookup product in database
                product = get_object_or_404(Product, id=product_id)
                # save to session
                cart.add(product=product, quantity=product_qty)
                # return a response
                # return JsonResponse({'Product Name': product.name})
                cart_quantity = cart.__len__()
                return JsonResponse({'Quantity': cart_quantity})
            except ValueError:
                # Handle the case where 'product_id' is not a valid integer
                return HttpResponseBadRequest("Invalid product ID")
        else:
            # Handle the case where 'product_id' is not provided
            return HttpResponseBadRequest("Product ID is required")

def cart_delete(request):
    pass

def cart_update(request):
    pass
