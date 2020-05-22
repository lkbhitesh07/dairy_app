from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

class Profile(models.Model):
    CHOICE = (
        ('Morning', 'Morning'),
        ('Evening', 'Evening'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(blank=False, max_length=25)
    last_name = models.CharField(blank=False, max_length=25)
    time = models.CharField( max_length=10, choices=CHOICE, blank=False)
    address = models.TextField(blank=False)
    contact_no = models.IntegerField(unique=True, blank=False)
    joining_date = models.DateField(default=datetime.date.today)

    class Meta:
        verbose_name = ("profile")
        verbose_name_plural = ("profiles")
        ordering = ('-user',)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class CustomerLedger(models.Model):
    related_customer = models.ForeignKey(User, related_name='CustomerLedger', on_delete=models.CASCADE, null=True)
    date = models.DateField(default=datetime.date.today)
    price = models.IntegerField(default=0)
    quantity = models.FloatField(max_length=10, default=0.0)
    total = models.FloatField(max_length=10, default=0.0)

    def __Str__(self):
        return self.related_customer
