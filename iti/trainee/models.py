from django.db import models
from course.models import Course


class Trainee(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, blank=True, null=True)
    age = models.IntegerField()
    degree = models.DecimalField(decimal_places=2, max_digits=4)
    image = models.ImageField(upload_to='trainee', blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.PROTECT, default=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
