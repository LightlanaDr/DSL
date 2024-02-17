from django.shortcuts import render
from .forms import ContactForm

def index(request):
    data = {
        'title': 'Главная страница'
    }
    return render(request, 'main/indexTemp2.html')


def delivery(request):
    return render(request, 'main/delivery.html')

def contact(request):
    return render(request, 'main/contact_dsl.html')

def send_message(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            contact.save()
            return render(request, 'main/created_mes.html', {'contact': contact})
    else:
        form = ContactForm()
    return render(request, 'main/send_message.html', {'form': form})
