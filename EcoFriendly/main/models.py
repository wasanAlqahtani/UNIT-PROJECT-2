from django.db import models

# Create your models here.

#contact model 
class Contact(models.Model):
    first_name = models.CharField(max_length=1024)
    last_name = models.CharField(max_length=1024)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)