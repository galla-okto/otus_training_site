from django.db import models

class Trainer(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=200)
    data = models.TextField(max_length=400)

    def __str__(self):
        return self.name

class Workout(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class Schedule(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.PROTECT)
    trainer = models.ForeignKey(Trainer, on_delete=models.PROTECT)

    title = models.CharField(max_length=80)
    date_time_start = models.DateTimeField()
    date_time_end = models.DateTimeField()

    def __str__(self):
        return self.title







