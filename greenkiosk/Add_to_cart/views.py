from django.shortcuts import render, redirect
from .models import Add_to_cart
# from .forms import ProductCartGetForm
from datetime import datetime
from .models import Product

def view_cart(request):
    Add_to_cart = Add_to_cart.objects.all()
    
    total_cart_price = 0

    for item in Add_to_cart:
        item.total_price = item.product_price * item.product_quantity
        total_cart_price += item.total_price

    return render(request, "Add_to_cart/view_cart.html", {"Add_to_cart": Add_to_cart, "total_cart_price": total_cart_price})


def update_cart(request, id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart_item = Add_to_cart.objects.get(id=id)
        if quantity > 0:
            cart_item.product_quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
    return redirect('view_cart')



def remove_item(request, id):
    cart_item = Add_to_cart.objects.get(id=id)
    cart_item.delete()

    return redirect('view_cart')
def empty_cart(request):
    Add_to_cart.objects.all().delete()
    return redirect("view_cart")

def add_to_cart(request, id):
    product = Product.objects.get(id=id)

    cart_item = Add_to_cart (
        product_name = product.name,
        product_price = product.price,
        product_image = product.image,
        product_quantity = 1,
        date_added=datetime.now(),
    )
    cart_item.save()

    return redirect("products_list")
