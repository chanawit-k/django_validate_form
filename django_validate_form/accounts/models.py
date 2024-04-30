import re

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import (MaxValueValidator, MinLengthValidator,
                                    MinValueValidator)
from django.db import models


class User(AbstractUser):
    pass


def validate_favwebsiteurl(iurl):
    pattern = re.compile(r"^http\://[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,3}(/\S*)?$")
    if not re.fullmatch(pattern, iurl):
        raise ValidationError("Invalid URL! Example :www.google.com")


class RegisterUser(models.Model):
    username = models.CharField(max_length=15, verbose_name="User Name",
                                validators=[MinLengthValidator(5, message='Min Length of User Name is 5 letters!')])

    password = models.CharField(max_length=15, verbose_name="Password",
                                validators=[MinLengthValidator(5, message='Min Length of Password is 5 letters')])

    confirm_password = models.CharField(max_length=15, verbose_name="Confirm Password",
                                        validators=[MinLengthValidator(5, message='Min Length of Confirm Password is 5 letters')])

    gender = models.CharField(max_length=10, verbose_name="Gender")
    country = models.CharField(max_length=20, verbose_name="Country")
    date_of_birth = models.DateField(verbose_name="Date of Birth")

    email = models.EmailField(verbose_name="Email")
    postal_code = models.IntegerField(validators=[MinValueValidator(1000, message='Postal code must be greater than equal to 1000.'),
                                                  MaxValueValidator(99999, message='Postal code must be lesser than equal to 99999.')], verbose_name="Postal Code")

    phone_number = models.CharField(
        max_length=15, verbose_name="Phone Number")

    profile = models.TextField(verbose_name="Profile of User", blank=True)
    website_url = models.URLField(verbose_name="Website URL")
    terms_conditions = models.BooleanField(
        verbose_name="Terms & Conditions")
    favwebsite_url = models.CharField(
        max_length=256, validators=[validate_favwebsiteurl])
