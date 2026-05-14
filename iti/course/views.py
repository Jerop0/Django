from django.shortcuts import render, redirect
from .models import Course


def course_list(request):
    courses = Course.objects.all()
    return render(request, "course/course_list.html", {"courses": courses})


def course_details(request, id):
    course = Course.objects.get(ID=id)
    return render(request, "course/course_details.html", {"course": course})


def course_add(request):
    if request.method == "POST":
        Course.objects.create(
            name=request.POST["name"],
            code=request.POST["code"],
            track=request.POST["track"],
        )
        return redirect("Course_List")
    return render(request, "course/course_add.html")


def course_update(request, id):
    course = Course.objects.get(ID=id)
    if request.method == "POST":
        course.name = request.POST["name"]
        course.code = request.POST["code"]
        course.track = request.POST["track"]
        course.save()
        return redirect("Course_Details", id=id)
    return render(request, "course/course_update.html", {"course": course})


def course_delete(request, id):
    course = Course.objects.get(ID=id)
    if request.method == "POST":
        course.delete()
        return redirect("Course_List")
    return render(request, "course/course_delete.html", {"course": course})
