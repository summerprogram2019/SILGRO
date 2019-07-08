from django.db import models

# Create your models here.
class Type(models.Model):
    id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=20)


class UserAccount(models.Model):
    # Required information for registration
    email = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    # Optional details
    DOB = models.DateField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=50, blank=True)

    # User rating
    user_rating = models.IntegerField(max_length=2, default=0)


class UserFinancial(models.Model):
    email = models.CharField(max_length=40, unique=True)

    # Credit/debit card details
    card_name = models.CharField(max_length=20, blank=True)
    card_number = models.IntegerField(blank=True, null=True)
    card_expiry = models.DateField(blank=True, null=True)
    card_cvv = models.IntegerField(max_length=3, blank=True, null=True)
    billing_address = models.CharField(max_length=50, blank=True)


class Listing(models.Model):
    # create new listing details
    title = models.TextField(max_length=50)
    description = models.TextField()
    availability = models.DateField()
    rate = models.IntegerField()
    images = models.ImageField()

    # listing display information
    user_rating = models.IntegerField(max_length=2, default=0)
