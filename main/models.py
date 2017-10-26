from django.db import models

class SmsContent(models.Model):
    text = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.text + ' ' + str(self.date)

