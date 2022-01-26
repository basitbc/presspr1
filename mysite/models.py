from django.db import models


from django.core import validators
from django.core.exceptions import ValidationError

from django import forms
import os
import datetime


class Contact(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.name
