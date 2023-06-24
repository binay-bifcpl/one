from django.db import models
from django.contrib.auth.models import User

class Requisition(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    date = models.DateField()
    image = models.ImageField(upload_to='requisitions')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

