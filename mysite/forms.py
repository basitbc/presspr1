from django import forms
from . import models


class ContactForm(forms.ModelForm):
    firstname = forms.CharField(max_length=264, widget=forms.TextInput(
        attrs={'placeholder': 'First Name', 'class': 'form-control', 'id': 'fname'}))

    lastname = forms.CharField(max_length=264, widget=forms.TextInput(
        attrs={'placeholder': 'Last Name', 'class': 'form-control', 'id': 'lname'}))

    email = forms.CharField(max_length=264, widget=forms.TextInput(
        attrs={'placeholder': 'Email', 'class': 'form-control', 'id': 'email'}))

    phone = forms.CharField(max_length=264, widget=forms.TextInput(
        attrs={'placeholder': 'Phone', 'class': 'form-control', 'id': 'phone'}))

    message = forms.CharField(max_length=264, widget=forms.Textarea(
        attrs={"rows": 5, "cols": 20, 'placeholder': 'Write your message', 'class': 'form-control',
               'id': 'message'}))

    class Meta:
        fields = ('firstname', 'lastname', 'email', 'phone', 'message')
        model = models.Contact
