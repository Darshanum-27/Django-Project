from django.db import models

class UserData(models.Model):
    
    username = models.CharField(max_length=20, primary_key=True)
    email = models.EmailField(max_length=30,unique=True)
    password = models.CharField(max_length=16, blank=True)

    def __str__(self):
        return self.username