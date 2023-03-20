from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import datetime
class About(models.Model):

    img = models.ImageField(upload_to='about/')
    title = models.CharField(max_length=250)
    description = RichTextUploadingField()

    def __str__(self):
        return f"{self.title} - {self.description}"


class Class(models.Model):
    img = models.ImageField(upload_to='clases/')
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=150)
    age = models.CharField(max_length=150)
    groups = models.CharField(max_length=150)
    time = models.CharField(max_length=30)
    money = models.CharField(max_length=155)

    def __str__(self):
        return f'{self.title}'

class Class2(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    description=models.CharField(max_length=255)
    def str(self):
        return f'{self.name},{self.name}'

class Teachers(models.Model):
    img = models.ImageField(upload_to='')
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=150)
    tw = models.CharField(max_length=255, null=True,blank=True)
    fac = models.CharField(max_length=255, null=True,blank=True)
    In = models.CharField(max_length=255, null=True,blank=True)

    def __str__(self):
        return self.title

class Teacher(models.Model):
    img = models.ImageField(upload_to='teacher/')
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=150)
    def __str__(self):
        return f'{self.title}'



class Gallery(models.Model):
    img = models.ImageField(upload_to='gallerys/')

    def __int__(self):
        return self.img


class Blog(models.Model):
    img = models.ImageField(upload_to='blogs/')
    title = models.CharField(max_length=250)
    description = RichTextUploadingField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ContactUs(models.Model):
    email = models.EmailField(max_length=250)
    name = models.CharField(max_length=250)
    subject = models.CharField(max_length=255)
    massage = models.TextField(max_length=255)

    def __str__(self):
        return self.name
    





