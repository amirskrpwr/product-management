from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Product, Order
from .forms import ProductForm, OrderForm, AddProductForm


def home_view(request):
    return render(request, "home.html",{})

def about_view(request):
    return render(request, "about.html", {})

def contact_view(request):
    return render(request, "contact.html", {})

def product_details_view(request):
    return render(request, "product/product_details.html", {
        "products" : Product.objects.all()
    })

def product_details_id_view(request,id):
    product = Product.objects.get(id=id)
    return render(request, "product/product_details_id.html", {
        "product" : product
    })

def product_create_view(request):
    form = ProductForm(request.POST or None)        
    if form.is_valid():
        form.save()
        form = ProductForm()
    return render(request, "product/product_create.html", {"form":form})

def order_create_view(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        order = Order(
            customerName=form.cleaned_data["customerName"],
            date = form.cleaned_data["date"]
        )
        order.save()
        form = OrderForm()  
        return HttpResponseRedirect("../%i" %order.id)      
    return render(request, "order/order_create.html", {"form":form})

def product_edit_view(request):           
    return render(request, "product/product_edit.html",{"products":Product.objects.filter()})

def order_edit_view(request):
    return render(request, "order/order_edit.html",{"orders":Order.objects.filter()})

def order_details_view(request):
    return render(request, "order/order_details.html",{"orders":Order.objects.all()})

def order_details_id_view(request,id):
    return render(request, "order/order_details_id.html", {
        "order" : Order.objects.get(id=id)
    })

def product_edit_id_view(request, id):
    product = Product.objects.get(id=id)
    initial_values={
        "title": product.title,
        "price": product.price,
        "description": product.description,
        "orders": product.orders.all(),
    }
    form = ProductForm(request.POST or None, initial=initial_values, instance=product)
    if form.is_valid():        
        form.save()
        return HttpResponseRedirect("../../%i" %product.id)
    
    return render(request, "product/product_edit_id.html", {"form":form})

def order_edit_id_view(request, id):
    order = Order.objects.get(id=id)

    if request.method == 'POST':
        form = AddProductForm(request.POST or None)
        print(Product.objects.all())
        if "delete" or "add" in request.POST:
            if 'delete' in request.POST:
                if form.is_valid():
                    for product in form.cleaned_data['choices']:
                        order.product_set.remove(product)
                        order.save()
            if 'add' in request.POST:
                if form.is_valid():
                    for product in form.cleaned_data['choices']:
                        order.product_set.add(product)
                        order.save()
            return HttpResponseRedirect("../../%i" %id)
    
    return render(request, "order/order_edit_id.html", {
        "order":order,
        "products":Product.objects.all()
    })
    
    