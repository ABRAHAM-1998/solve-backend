from django.db import models

# Create your models here.

class UserLogin(models.Model):
    username = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    role = models.CharField(max_length=10, default='user')
    active_flag = models.IntegerField(default=1)


class ComplaintPriority(models.Model):
    priority_name = models.CharField(max_length=50)
    display_style = models.CharField(max_length=35, default='alert alert-info')
    active_flag = models.IntegerField(default=1)


class UserDetails(models.Model):
    email = models.CharField(max_length= 55)
    mobile = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    dob = models.CharField(max_length=20)
    fk_login = models.ForeignKey(UserLogin, on_delete=models.CASCADE)


class Complaintreg(models.Model):
    complaint = models.TextField()
    fk_priority = models.ForeignKey(ComplaintPriority, on_delete=models.CASCADE)
    fk_user = models.ForeignKey(UserLogin, on_delete=models.CASCADE)
    active_flag = models.IntegerField(default=1)


class ComplaintImages(models.Model):
    image = models.FileField(upload_to='uploads/')
    fk_complaint = models.ForeignKey(Complaintreg, on_delete=models.CASCADE)