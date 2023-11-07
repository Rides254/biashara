from django.db import models

# Create your models here.

class Member(models.Model):
      firstname=models.CharField(max_length=50)
      lastname=models.CharField(max_length=50)
      email=models.EmailField()
      username=models.CharField(max_length=50)
      password=models.CharField(max_length=50)


      def __str__(self):
          return self.firstname +" " +self.lastname


class Product(models.Model):
      name = models.CharField(max_length=25)
      price = models.IntegerField(default=0)
      description = models.TextField()

      def __str__(self):
            return self.name