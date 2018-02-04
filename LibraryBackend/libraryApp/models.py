
from django.db import models

# Create your models here.

#model book to store information about book like name, author, isbn no, description.
class book(models.Model):
    name=models.CharField(max_length=40)
   # id=models.IntegerField(primary_key=True)
    author=models.CharField(max_length=25)
    isbn_no=models.IntegerField(primary_key=True,default=1000)
    description=models.CharField(max_length=300)
    def __str__(self):
        return self.name

#model author_info to add information about authors like name, gender, age, place of birth
class author_info(models.Model):
    GENDER_CHOICE=(
        ('M','Male'),
        ('F','Female'),
    )
    name=models.CharField(max_length=40)
    id = models.AutoField(primary_key=True)
    #id=models.IntegerField(primary_key=True)
    pob=models.CharField(max_length=20,default='india')
    gender=models.CharField(max_length=2,choices=GENDER_CHOICE)
    #dob=models.DateField()
    age = models.IntegerField(default=25)

    def __str__(self):
        return self.name

