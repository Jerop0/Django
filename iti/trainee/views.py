from django.shortcuts import render, redirect
from .models import Trainee
from .forms import TraineeForm
from course.models import Course


def trainee_list(request):
    students = Trainee.objects.all()
    return render(request, "trainee/trainee_list.html", {"students": students})


def trainee_details(request, id):
    trainee = Trainee.objects.get(ID=id)
    return render(request, "trainee/trainee_details.html", {"trainee": trainee})


def trainee_add(request):
    if request.method == "POST":
        Trainee.objects.create(
            name=request.POST["name"],
            age=request.POST["age"],
            degree=request.POST["degree"],
            image=request.FILES.get("image"),
            course=Course.objects.get(pk=request.POST["course"]),
        )
        return redirect("Trainee_List")
    return render(request, "trainee/trainee_add.html")


def trainee_AddForm(request):
    context = {"trainees": Trainee.objects.all(), "form": TraineeForm()}
    if request.method == "POST":
        form = TraineeForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            Trainee.objects.create(
                name=request.POST["name"],
                age=request.POST["age"],
                degree=request.POST["degree"],
                image=request.FILES.get("image"),
                course=Course.objects.get(pk=request.POST["course"]),
            )
            return redirect("Trainee_List")
    return render(request, "trainee/trainee_add.html", context=context)


def trainee_update(request, id):
    trainee = Trainee.objects.get(ID=id)
    if request.method == "POST":
        trainee.name = request.POST["name"]
        trainee.age = request.POST["age"]
        trainee.degree = request.POST["degree"]
        trainee.image = request.FILES.get("image", trainee.image)
        trainee.course = Course.objects.get(pk=request.POST["course"])
        trainee.save()
        return redirect("Trainee_Details", id=id)
    return render(request, "trainee/trainee_update.html", {"trainee": trainee, "courses": Course.objects.all()})


def trainee_delete(request, id):
    trainee = Trainee.objects.get(ID=id)
    if request.method == "POST":
        trainee.delete()
        return redirect("Trainee_List")
    return render(request, "trainee/trainee_delete.html", {"trainee": trainee})
