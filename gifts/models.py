from django.db import models

# Create your models here.

class Gifts(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=300)
    description = models.TextField()
    taken = models.BooleanField()
    url = models.URLField(max_length=300)
    image = models.ImageField(upload_to='images', null=True)
    instruction = models.TextField(null=True)

    def __str__(self):
        return f'{self.title} - {self.id}'