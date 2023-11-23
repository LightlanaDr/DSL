from django import forms
from .models import NewOrder

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 6)]


class CartAddProductForm(forms.Form):
    # quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    quantity = forms.IntegerField(label="", max_value=6, min_value=1, initial=1,
                                  widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                  'style': 'width: 30%; '
                                                                  'text-align: center;'}))
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

    # class Meta:
    #     widgets = {
    #         'quantity': forms.NumberInput(attrs={'class': 'form-control', 'size': 10, }),
    #     }


class OrderCreate(forms.ModelForm):
    class Meta:
        model = NewOrder
        fields = ['first_name', 'last_name', 'email', 'phone', 'address']
        labels = {'first_name': 'Имя', 'last_name': 'Фамилия',
                  'email': 'Эл.почта', 'phone': 'Тел.', 'address': 'Адрес'}

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Имя'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Фамилия'}),

            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'placeholder': 'Эл. адрес'}),
            'phone': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': '+7...'}),
            'address': forms.TextInput(attrs={'class': 'form-control',
                                              'placeholder': 'Адрес доставки'}),

        }
