from django import forms
from .models import Order, Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "orders",
            "title",
            "description",
            "price",
        ]

class RawProductForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField()
    sammary = forms.CharField()

class AddProductForm(forms.Form):
    choices = forms.ModelMultipleChoiceField(
        queryset = Product.objects.all(),
        widget  = forms.CheckboxSelectMultiple,
    )

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "date",
            "customerName",
        ]