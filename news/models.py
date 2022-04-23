from django.db import models

class News(models.Model):
    headline = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateField(auto_created=True)

    def __str__(self):
        return self.headline