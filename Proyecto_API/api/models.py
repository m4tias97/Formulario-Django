from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=5, null=False)
    lastname=models.CharField(max_length=50, blank=True, null=False)
    email = models.EmailField(blank=True, null=False)
    phone=models.CharField(max_length=50, blank=True, null=False)

    def __str__(self):
        return (self.name)
        
        
        
