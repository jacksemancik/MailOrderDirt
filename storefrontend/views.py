from django.shortcuts import render_to_response
from storefrontend.models import Products

# Create your views here.
def homeserve(request):
    products = Products.objects.all()
    return render_to_response('home.html', {'products': products})

def productserve(request, value):
    productpage = Products.objects.filter(slug=value)
    if productpage:
        name = productpage['name']
        description = productpage['description']
        price = productpage['price']
        image = productpage['imagepath']
        return render_to_response('product.html', {'name':name,'description':description,'price':price,'image':image})
    else:
        return render_to_response('404.html', value)
