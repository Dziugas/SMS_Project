from django.db import models

class Notes(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title

