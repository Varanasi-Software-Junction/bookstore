from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name} - ₹{self.price}"