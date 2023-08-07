from django.db import models

# Create your models here.

class notepad(models.Model):
    note_tittle = models.CharField(max_length=500)
    note_desc = models.CharField(max_length= 5000)


