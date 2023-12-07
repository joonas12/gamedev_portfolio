from django.db import models

# Create your models here.
<<<<<<< HEAD
# moro
=======
class Testi(models.Model):
    description = models.CharField(max_length=8)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.description
>>>>>>> origin/main
