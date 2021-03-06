from django import forms

class ContactForm(forms.Form):
    username = forms.CharField(required=True, label="name")
    usermail = forms.EmailField(required=True, label="email")
    phone = forms.CharField(required = True, label="phone")
    message = forms.CharField(
        required=True,
        widget=forms.Textarea,
        label="message"
    )

class DonateForm(forms.Form):
    username = forms.CharField(required=True, label="username")
    usermail = forms.EmailField(required=True, label="usermail")
    subject = forms.CharField(required = True, label="subject")
    message = forms.CharField(
        required=True,
        widget=forms.Textarea,
        label="message"
    )
