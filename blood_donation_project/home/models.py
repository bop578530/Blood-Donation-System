from django.db import models

# Create your models here.

class contact(models.Model):
    name= models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    msg= models.TextField()

class Donateblood(models.Model):
    fname= models.CharField(max_length= 50)
    email= models.CharField(max_length=50)
    date= models.DateField()
    blood_group_choice= (
        ("A+", "A+"),
        ("A-", "A-"),
        ("B-","B-"),
        ("B-", "B+"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
        ("O-", "O-"),
        ("O+", "O+"),
    )
    bloodGroup= models.CharField(choices= blood_group_choice, max_length= 50, blank= True)
    contactNumber= models.CharField(max_length=10)

class requestBlood(models.Model):
    fullname= models.CharField(max_length= 50, default='')
    email= models.CharField(max_length=50)
    blood_group_choice= (
        ("A+", "A+"),
        ("A-", "A-"),
        ("B-","B-"),
        ("B-", "B+"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
        ("O-", "O-"),
        ("O+", "O+"),
    )
    bloodGroup= models.CharField(choices= blood_group_choice, max_length= 50, blank= True)
    contactNumber= models.CharField(max_length=10)
    quantity= models.CharField(max_length=50)
    urgency= models.CharField(max_length=50)
    desc= models.CharField(max_length=50)