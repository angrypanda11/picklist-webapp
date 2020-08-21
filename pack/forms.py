from django import forms

from .models import Order, Dictionary

PICKED = [
        ('以捡', '以捡'),
        ('未捡', '未捡'),
    ]


class OrderUpdateForm(forms.ModelForm):
    picked = forms.ChoiceField(required=False, widget=forms.RadioSelect, choices=PICKED)
    notes = forms.CharField(required=False)

    class Meta:
        model = Order
        fields = [
            'picked',
            'notes',
        ]


class DictionaryUpdateForm(forms.ModelForm):
    class Meta:
        model = Dictionary
        fields = [
            'sku',
            'product_code',
            'multiplier',
            'price',
        ]
