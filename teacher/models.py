from django.db import models

class Teacher(models.Model):
      name=models.CharField(max_length=32)
      qualification=models.CharField(max_length=32)
      subject=models.CharField(max_length=32)
      age=models.IntegerField()
 
      def __str__(self):
           return self.name