from django.db import models

# Create your models here.
class Testi(models.Model):
    description = models.CharField(max_length=8)

    def __str__(self):
        return self.description