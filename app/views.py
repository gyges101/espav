from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def presentation(request):

    return render(request, 'presentation.html', {})

def equipement(request):

    return render(request, 'equipement.html', {})

def inscription(request):

    return render(request, 'inscription.html', {})

def press(request):

    return render(request, 'press.html', {})

def prodvisuel(request):

    return render(request, 'prodvisuel.html', {})

def allform(request):

    return render(request, 'allform.html', {})

def agenda(request):

    return render(request, 'agenda.html', {})

def faq(request):

    return render(request, 'faq.html', {})

def contact(request):

    return render(request, 'contact.html', {})