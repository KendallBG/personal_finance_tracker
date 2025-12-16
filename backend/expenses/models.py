from django.db import models

# Create your models here.

class Expense (models.Model):
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    date = models.CharField()
    created_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return f"{self.title} - {self.amount}"