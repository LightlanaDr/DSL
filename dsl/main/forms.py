from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'tel', 'email', 'message']
        labels = {'first_name': 'Имя', 'last_name': 'Фамилия', 'tel': 'Тел.',
                  'email': 'Эл.почта', 'message': 'Сообщение'}

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Иван'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Иванов'}),
            'tel': forms.TextInput(attrs={'class': 'form-control',
                                          'placeholder': '+7...'}),

            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'placeholder': '1@mail.ru'}),
            'message': forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': 'Я хочу,...'}),

        }
