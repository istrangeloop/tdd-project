from django.db import models

# Create your models here.
class User(models.Model):

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    is_anonymous = False
    is_authenticated = True
    email = models.EmailField(primary_key=True)
