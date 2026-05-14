from django.db import models


class Trainee(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    degree = models.DecimalField(decimal_places=2, max_digits=4)

    def __str__(self):
        return self.name
