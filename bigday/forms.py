from django import forms

class ContactForm(forms.Form):
    username = forms.CharField(required=True, label="username")
    usermail = forms.EmailField(required=True, label="usermail")
    subject = forms.CharField(required = True, label="subject")
    message = forms.CharField(
        required=True,
        widget=forms.Textarea,
        label="message"
    )
    
