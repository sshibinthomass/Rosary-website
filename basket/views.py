from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from store.models import Product

from .basket import Basket


def basket_summary(request):
    basket = Basket(request)
    print("1")
    if request.method == 'POST':
        if(request.POST["button1"]=="Add to cart"):
            print("added")

    return render(request, 'store/basket/summary.html', {'basket': basket})

def basket_add(request):
    print("2")
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        print(request.POST.get('productqty'))
        print("Helo1")
        print("Helo2")
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        print(product_id)
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)

        basketqty = basket.__len__()
        response = JsonResponse({'qty': basketqty})
        return response


def basket_delete(request):
    print("3")
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        basket.delete(product=product_id)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response


def basket_update(request):
    print("4")
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        basket.update(product=product_id, qty=product_qty)

        basketqty = basket.get_total()
        print(basketqty)
        baskettotal = basket.get_total_price()
        print(baskettotal)
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response
    