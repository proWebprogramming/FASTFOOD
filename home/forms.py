from django import forms
from home.models import ContactMessage
from product.models import Order

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ( 'name', 'surname', 'email', 'phone',  'message',)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ( 'name','surname','phone','amount','category', 'food', 'address',)