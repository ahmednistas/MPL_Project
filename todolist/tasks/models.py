from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
'''
class CusUser(AbstractBaseUser):
    STATUS = (
        ('normal','normal'),
        ('admin','admin')
    )
    
    email = models.EmailField(unique=True)
    status = models.CharField(max_length=100,choices=STATUS,default='normal')
    description = models.TextField('description', max_length=600, default='',blank=True)

    def __str__(self):
        return self.username
'''
'''
class User(models.Model):
    UType_choices = [("admin", "admin"), ("user", "user")]
    UserID = models.IntegerField(primary_key=True)
    UEmail = models.EmailField(unique=True, null=False)
    UName = models.CharField(max_length=150)
    UPassword = models.CharField(max_length=150)
    UType = models.CharField(choices=UType_choices, max_length=150, null=False)
'''



class Task(models.Model):
    Repeat_choices = [("Daily", "Daily"), ("Weekdays", "Weekdays"), ("Weekly", "Weekly"), ("Monthly", "Monthly"),
                      ("Yearly", "Yearly")]
    Category_choices = [("Blue", "Blue"), ("Green", "Green"), ("Orange", "Orange"), ("Purple", "Purple"),
                        ("Red", "Red"), ("Yellow", "Yellow")]
    Priority_choices = [("High", "High"), ("Low", "Low")]
    Status_choices = [("Checked", "Checked"), ("unChecked", "unChecked")]
    TaskID = models.AutoField(primary_key=True)
    UserID = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    TName = models.CharField(max_length=150)
    DueDate = models.DateField(null=True)
    created_at = models.DateField(default=datetime.date.today())
    Repeat = models.CharField(choices=Repeat_choices, max_length=20, null=True)
    Priority = models.CharField(choices=Priority_choices, max_length=20, default="Low")
    Status = models.CharField(choices=Status_choices, max_length=20, default="unChecked")
    Category = models.CharField(choices=Category_choices, max_length=20, null=True)
    Description = models.CharField(max_length=1000, null=True)

