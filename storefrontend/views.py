from django.conf import settings
from django.shortcuts import render_to_response
from storefrontend.models import Products, About, Skills, ContactModel
from storefrontend.forms import ContactForm
from mailorderdirt.settings import CONTACT_RECIPIENT

# Create your views here.
def homeserve(request):
    products = Products.objects.all()
    about_text = About.objects.get(id=1)
    skills = Skills.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            sender = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message_content = form.cleaned_data['message']
            message = 'The following message was sent from %s %s (%s):<br /> %s' % (first_name, last_name, sender, message_content)
            recipient = CONTACT_RECIPIENT
            ContactModel.objects.create(first_name=first_name, last_name=last_name, sender=sender, subject=subject, message=message_content)
            send_mail(subject, message, sender, recipient)
            confirmation = 'Thanks! Your message has been sent!'
            return render_to_response('home.html', {'products': products, 'about_text':about_text, 'skills':skills, 'form':confirmation})
    else:
        form = ContactForm()
        return render_to_response('home.html', {'products': products, 'about_text':about_text, 'skills':skills, 'form':form})

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
