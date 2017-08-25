from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=50)
    last_name = forms.CharField(label="Last Name", max_length=50)
    email = forms.EmailField(label="Email")
    subject = forms.CharField(label="Subject", max_length=100)
    message = forms.CharField(label="Message", widget=forms.Textarea)
