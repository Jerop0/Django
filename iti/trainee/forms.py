from django import forms
from .models import Trainee
from course.models import Course


class TraineeForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    degree = forms.DecimalField(decimal_places=2, max_digits=4)
    image = forms.ImageField(label="Profile image")
    course = forms.ChoiceField(choices=[(c.ID, c.name) for c in Course.objects.all()])


class TraineeFormModel(forms.ModelForm):
    class Meta:
        model = Trainee
        fields = ["name", "age", "degree", "image", "course"]
