from django.db import models


class Expense(models.Model):
    title = models.CharField(max_length=50)
    image_url = models.URLField()
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return f'{self.title}'
