from django.db import models

# Create your models here.
class TextReplace(models.Model):
    wantReplace = models.CharField(max_length=100)
    withReplace = models.CharField(max_length=100)
    textFile = models.FileField(upload_to='files/texts/')

    def __str__(self):
        return self.title
