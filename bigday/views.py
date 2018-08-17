from django.core.mail import BadHeaderError, EmailMessage
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm, DonateForm
from django.contrib import messages

def home(request):
    return render(request, './home.html',{})

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
	    #messages.success(request,'Form submission successful')
            contact_name = form.cleaned_data['username']
            contact_email = form.cleaned_data['usermail']
	    #contact_subject = form.cleaned_data['subject']
            content = form.cleaned_data['message']
            try:
                email = EmailMessage(contact_name,
                                    content,
                                    contact_email,
                                    ['protostartup@gmail.com'], #change to your email
                                     reply_to=[contact_email],
                                   )
                email.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/thanks/')
    return render(request, 'partials/newcontact.html', {'form': form})


def thanks(request):
    return render(request, './home.html', {})

def donate(request):
    if request.method == 'GET':
        form = DonateForm()
    else:
        form = DonateForm(request.POST)
        if form.is_valid():
            #messages.success(request,'Form submission successful')
            contact_name = form.cleaned_data['username']
            contact_email = form.cleaned_data['usermail']
            #contact_subject = form.cleaned_data['subject']
            content = form.cleaned_data['message']
            try:
                email = EmailMessage(contact_name,
                                    content,
                                    contact_email,
                                    ['protostartup@gmail.com'], #change to your email
                                     reply_to=[contact_email],
                                   )
                email.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/thanks/')
    return render(request, 'partials/newdonate.html', {'form': form})

