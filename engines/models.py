from django.db import models


class Engine(models.Model):
    name = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=200)
    thrust_newtons_sea_level = models.DecimalField(max_digits=19, decimal_places=2, default=0.00)
    thrust_newtons_vacuum = models.DecimalField(max_digits=19, decimal_places=2, default=0.00)
    specific_impulse_sea_level = models.IntegerField(default=0)
    specific_impulse_vacuum = models.IntegerField(default=0)
    image_url = models.URLField(max_length=200)

    def __str__(self):
        return f'{self.manufacturer} {self.name}'


class Rocket(models.Model):
    engines = models.ManyToManyField(Engine, through='RocketEngine')
    name = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=200)
    image_url = models.URLField(max_length=200)

    def __str__(self):
        return f'{self.manufacturer} {self.name}'


class RocketEngine(models.Model):
    rocket = models.ForeignKey(Rocket, on_delete=models.CASCADE)
    engine = models.ForeignKey(Engine, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    stage  = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.rocket.manufacturer} {self.rocket.manufacturer} stage {self.stage}: {self.amount} engine(s)'
