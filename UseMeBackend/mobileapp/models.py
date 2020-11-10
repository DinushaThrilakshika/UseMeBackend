from django.db import models

class Customer(models.Model):
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    confirm_password = models.CharField(max_length=20)
    email_address = models.CharField(max_length=30)
    home_address = models.CharField(max_length=30)
    account_number = models.IntegerField()
    mobile_number = models.IntegerField()

class Shop(models.Model):
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    confirm_password = models.CharField(max_length=20)
    owner_email_address = models.CharField(max_length=30)
    shop_address = models.CharField(max_length=30)
    shop_number = models.IntegerField()
    mobile_number = models.IntegerField()

def upload_path(instance,filename):
    return '/'.join(['covers',str(instance.user_name),filename])

class Dperson(models.Model):
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    confirm_password = models.CharField(max_length=20)
    email_address = models.CharField(max_length=30)
    home_address = models.CharField(max_length=30)
    vehicle_type = models.CharField(max_length=20)
    vehicle_number = models.CharField(max_length=10)
    mobile_number = models.IntegerField()
    licens = models.ImageField(blank=True,null=True,upload_to=upload_path)
    photo = models.ImageField(blank=True,null=True,upload_to=upload_path)
    


def __str__(self):
    return self.user_name