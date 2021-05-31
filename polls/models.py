from django.db import models


class Account(models.Model):
    login = models.CharField(max_length=50, null=False, blank=False)
    password = models.CharField(max_length=50, null=False, blank=False)
    active = models.BooleanField(default=True)


class Employee(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    add_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    account = models.OneToOneField(Account, on_delete=models.DO_NOTHING)
    cars = models.ManyToManyField("Car")


class Phone(models.Model):
    phone = models.CharField(max_length=20)
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)


class Car(models.Model):
    model = models.CharField(max_length=50)
    price = models.FloatField()
# ctrl+Alt+R
