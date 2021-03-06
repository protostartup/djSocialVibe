from django.core.mail import BadHeaderError, EmailMessage
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm, DonateForm
from django.contrib import messages

def home(request):
    return render(request, './index.html',{})

def volunteer(request):
    return render(request, './volunteer.html',{})

def donate(request):
    return render(request, './donate.html',{})


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm()
        form.username=request.POST.get('name')
        form.email=request.POST.get('email')
        form.phone=request.POST.get('phone')
        form.message=request.POST.get('message')

        try:
            email = EmailMessage(subject = form.username,
                                 body =form.message+" "+form.phone,
                                 from_email='protostartup@gmail.com', #change to your email
                                 to=['protostartup@gmail.com'],
                                 reply_to=[form.email],
                                 #headers = form.phone
                                 )
            email.send()
        except BadHeaderError:
            print("err")
            return HttpResponse('Invalid header found.')
        return redirect('/thanks/')
    return render(request, './donate.html', {'form': form})


def thanks(request):
    return render(request, './index.html', {})

# def donate(request):
#     if request.method == 'GET':
#         form = DonateForm()
#     else:
#         form = DonateForm(request.POST)
#         if form.is_valid():
#             #messages.success(request,'Form submission successful')
#             contact_name = form.cleaned_data['username']
#             contact_email = form.cleaned_data['usermail']
#             #contact_subject = form.cleaned_data['subject']
#             content = form.cleaned_data['message']
#             try:
#                 email = EmailMessage(contact_name,
#                                     content,
#                                     contact_email,
#                                     ['protostartup@gmail.com'], #change to your email
#                                      reply_to=[contact_email],
#                                    )
#                 email.send()
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#             return redirect('/thanks/')
#     return render(request, 'donate.html', {'form': form})
