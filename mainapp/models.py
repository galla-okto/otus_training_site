from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

UserModel = get_user_model()


class Trainer(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=200)
    data = models.TextField()

    def __str__(self):
        return self.name


class Workout(models.Model):
    ALL = 'l'
    BEGINNER = 'b'
    INTERMEDIATE = 'i'
    ADVANCED = 'a'
    LEVELS = (
        (ALL, 'All'),
        (BEGINNER, 'Beginner'),
        (INTERMEDIATE, 'Intermediate'),
        (ADVANCED, 'Advanced'),
    )

    name = models.CharField(max_length=80)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    duration_lesson = models.DecimalField(max_digits=3, decimal_places=1)
    quantity_lesson = models.IntegerField()
    initial_level = models.CharField(max_length=1, choices=LEVELS, default=ALL)
    star_rating = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('mainapp:index', kwargs={'pk': self.pk})
        return reverse('mainapp:index')


class Schedule(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.PROTECT)
    trainer = models.ForeignKey(Trainer, on_delete=models.PROTECT)

    title = models.CharField(max_length=80)
    date_time_start = models.DateTimeField()
    date_time_end = models.DateTimeField()

    def __str__(self):
        return self.title

    def clients_count(self):
        return len(self)


class Client(models.Model):
    nick = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    user = models.OneToOneField(UserModel, on_delete=models.PROTECT)

    def __str__(self):
        return self.user.username


class Enrollment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    schedule = models.ForeignKey(Schedule, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.client} / {self.schedule}'




