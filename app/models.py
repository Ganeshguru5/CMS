
from django.db import models
from django.db.models.aggregates import Max
from django.db.models.base import Model
from django.db.models.fields import EmailField, IntegerField
from django.db import IntegrityError, models, router, transaction


# Create your models here.
class Candidate_details(models.Model):
     
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    emaiid=models.CharField(max_length=50)
    Department=models.CharField(max_length=20)
    mobilenum=models.CharField(max_length=10)
    

class Organiser_details(models.Model):
     
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    emaiid=models.CharField(max_length=50)
    Department=models.CharField(max_length=20)
    mobilenum=models.CharField(max_length=10)


class Reviewer_details(models.Model):
     
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    emaiid=models.CharField(max_length=50)
    Department=models.CharField(max_length=20)
    mobilenum=models.CharField(max_length=10)

class submitted_papers(models.Model):
    # 
    Name=models.CharField(max_length=20)
    Topic=models.CharField(max_length=20)
    Url=models.URLField()
    Department=models.CharField(max_length=20)
    emaiid=models.CharField(max_length=50)

class selected_paper(models.Model):
    Reviewer=models.CharField(max_length=20)
    Name=models.CharField(max_length=20)
    Topic=models.CharField(max_length=20)
    Url=models.URLField()
    Department=models.CharField(max_length=20)
    emaiid=models.CharField(max_length=50)

class reviewed_papers(models.Model):
    Name=models.CharField(max_length=20)
    Topic=models.CharField(max_length=20)
    Url=models.URLField()
    Department=models.CharField(max_length=20)
    emaiid=models.CharField(max_length=50)
    

class paymentdetails(models.Model):
    Name=models.CharField(max_length=20)
    Topic=models.CharField(max_length=20)
    emaiid=models.CharField(max_length=50)
   
    card_number=models.CharField(max_length=30)
    amountpaid=models.CharField(max_length=10)

class returned_papers(models.Model):
    Name=models.CharField(max_length=20)
    Topic=models.CharField(max_length=20)
    Url=models.URLField()
    Department=models.CharField(max_length=20)
    emaiid=models.CharField(max_length=50)
