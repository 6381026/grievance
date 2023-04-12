from django.db import models

# Create your models here.
class box(models.Model):
   name = models.CharField(max_length=255)
   email = models.CharField(max_length=255)
   message = models.CharField(max_length=255)
   date = models.DateField()
   time = models.TimeField()
   toemail = models.CharField(max_length=255)

   def __str__(self):
      return self.name

class suggestion(models.Model):
   name = models.CharField(max_length=255)
   email = models.CharField(max_length=255)

   def __str__(self):
      return self.name
