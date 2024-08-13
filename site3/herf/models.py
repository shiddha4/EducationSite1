from django.db import models


# Create your models here.


class students(models.Model):
    name = models.CharField(max_length=255)
    belt = models.CharField(max_length=255)
    days = models.CharField(max_length=255)
    enrollDate = models.CharField(max_length=255)
    notes = models.TextField(null=True)



class classes(models.Model):
    name = models.CharField(max_length=255)
    date_today = models.DateTimeField(null=True)
    ssn = models.ForeignKey(students, on_delete=models.CASCADE)

class daysNumbers(models.Model):
    ssn_15 = models.ForeignKey(students, on_delete=models.CASCADE)
    days=models.IntegerField(default=0)

