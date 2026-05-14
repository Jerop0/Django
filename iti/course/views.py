from django.shortcuts import render


def course_list(request):
    context = {"courses": [{"id": 1, "name": "python"}, {"id": 2, "name": "django"}, {"id": 3, "name": "apache"}]}
    return render(request, "course/course_list.html", context)


def course_add(request):
    return render(request, "course/course_add.html")


def course_update(request, id):
    return render(request, "course/course_update.html", {"id": id})


def course_delete(request, id):
    return render(request, "course/course_delete.html", {"id": id})
