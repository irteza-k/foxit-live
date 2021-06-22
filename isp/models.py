from django.db import models
from django.utils import timezone
# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    balance  = models.CharField(max_length=100)
    location = models.CharField(max_length=500)
    password = models.CharField(max_length=200, default='1234')
    connection_date = models.DateTimeField(default = timezone.now())
    phone_no = models.IntegerField()
    st = (
        ('S', 'Suspended'),
        ('O', 'Overdue'),
        ('A', 'Active'),
        ('D', 'Deactive')
    )
    status = models.CharField(max_length=1, choices=st)

    ut = (
        ('A', 'admin'),
        ('G', 'general'),
        ('V', 'vip')
    )
    user_type =  models.CharField(max_length=1, choices=ut)


class Packages(models.Model):
    price = models.CharField(max_length = 100, default='0')
    bandwidth = models.CharField(max_length=500)
    extra_information = models.TextField()

class Invoices(models.Model):
    total_balance = models.CharField(max_length=100, default='0')
    month = models.CharField(max_length=100, default='0')
    Date_issued = models.DateTimeField(default = timezone.now())
    date_auto_disconnect = models.DateTimeField(default = timezone.now())
    is_paid = models.BooleanField(default=False)
    st = (
        ('B', 'Bkash'),
        ('C', 'Credit_Card'),
        ('D', 'cash_on_delivery')
    )
    payment_type = models.CharField(max_length=1, choices=st, default = 'B')


class UserAndinvoice(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    invoice_id = models.ForeignKey(Invoices, on_delete=models.CASCADE)
