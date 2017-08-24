from django.conf import settings
from django.shortcuts import render_to_response
from storefrontend.models import Products, About, Skills

# Create your views here.
def homeserve(request):
    products = Products.objects.all()
    about_text = About.objects.get(id=1)
    skills = Skills.objects.all()
    return render_to_response('home.html', {'products': products, 'about_text':about_text, 'skills':skills})

def productserve(request, value):
    productpage = Products.objects.filter(slug__exact=value)
    if productpage:
        #name = productpage['name']
        #description = productpage['description']
        #price = productpage['price']
        #image = productpage['image']
        return render_to_response('product.html', {'product':productpage})
    else:
        return render_to_response('404.html', value)
