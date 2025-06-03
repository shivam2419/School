from django.db import models

# Create your models here.
# Contact page form
class Contact(models.Model):
    user_id=models.AutoField
    f_name=models.CharField(max_length=200)
    l_name=models.CharField(max_length=200) 
    email=models.EmailField()
    pnum =models.CharField(max_length=400)

class event(models.Model):
    event_id=models.AutoField

    date=models.IntegerField()
    month=models.CharField(max_length=20)

    event=models.CharField(max_length=20)
    event_desc = models.CharField(max_length=2000, null=True)
    event_img=models.ImageField(upload_to='events/images',default="")
    created_at = models.DateTimeField(auto_now_add=True)

class activity(models.Model):
    activity=models.ImageField(upload_to='activity/images',default="")
    created_at = models.DateTimeField(auto_now_add=True)

class notice(models.Model):
    date=models.CharField(max_length=100)
    notice=models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

#Registration data model
class registration(models.Model):
    student_name=models.CharField(max_length=50)
    father_name=models.CharField(max_length=50)
    mother_name=models.CharField(max_length=50)
    dob=models.CharField(max_length=10)
    phone_number=models.IntegerField()
    email_id=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    class_for=models.CharField(max_length=50)
    last_schl=models.CharField(max_length=80)
    last_schl=models.CharField(max_length=80)
    address=models.CharField(max_length=100)
    trans_req=models.CharField(max_length=10)

# School Gallery
class inaugration(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    inaugration=models.ImageField(upload_to='activity/images',default="")

class assembly(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    assembly=models.ImageField(upload_to='activity/images',default="")

class function(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    function=models.ImageField(upload_to='activity/images',default="")

class Pt(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    Pt=models.ImageField(upload_to='activity/images',default="")