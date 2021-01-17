from django.db import models

class Trainer(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    data = models.TextField(max_length=200)

    @property
    def __str__(self):
        return self.name

