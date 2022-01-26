from django.contrib.messages.api import success
from django.http.response import HttpResponse
from .models import Contact
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from collections import namedtuple
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, DeleteView, DetailView
from . import models
from . import forms
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def news(request):
    return render(request, 'news.html')


def practivities(request):
    return render(request, 'practivities.html')


def contact(request):
    contact = models.Contact.objects.all()
    form = forms.ContactForm()

    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        New = Contact(
            firstname=firstname,
            lastname=lastname,
            email=email,
            phone=phone,
            message=message)

        data = {
            'firstname': firstname,
            'lastname': lastname,
            'email': email,
            'phone': phone,
            'message': message
        }

        message = '''
        The message is sent by: {} {}

        Email_id: {}
        Phone No: {}
        Message: {}

        '''.format(data['firstname'], data['lastname'], data['email'], data['phone'], data['message'])
        send_mail(data['email'], message, '', ['bbchanna@gmail.com'])

        form = forms.ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form = forms.ContactForm()
            messages.success(
                request, 'Thanks for your Message.We will reach back to you soon.')
            success = 'Thanks for your Message.We will reach back to you soon.'
            return HttpResponse(success)
            # return render(request, 'contact.html', {'form': form})

    context = {'form': form}
    return render(request, 'contact.html', context)
