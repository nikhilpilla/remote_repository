from django.db import models

class ContactData(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=100)
class ServicerData(models.Model):
    courseno=models.IntegerField()
    coursename=models.CharField(max_length=100)
    fee=models.IntegerField()
    faculty=models.CharField(max_length=100)
    timeduration=models.IntegerField()
    def __str__(self):
        return self.coursename
