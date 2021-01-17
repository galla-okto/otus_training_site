from django.db import models

class Trainer(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    data = models.TextField(max_length=200)

    @property
    def __str__(self):
        return self.name

class Workout(models.Model):
    name = models.CharField(max_length=80)

    @property
    def __str__(self):
        return self.name

class Schedule(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.PROTECT)
    trainer = models.ForeignKey(Trainer, on_delete=models.PROTECT)

    date_start = models.DateField()
    date_end = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()

    def __str__(self):
        return self.workout







