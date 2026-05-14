from django.shortcuts import render


def trainee_list(request):
    context = {"students": [{"id": 1, "name": "ahmed"}, {"id": 2, "name": "mohamed"}, {"id": 3, "name": "yamen"}]}
    return render(request, "trainee/trainee_list.html", context)


def trainee_add(request):
    return render(request, "trainee/trainee_add.html")


def trainee_update(request, id):
    return render(request, "trainee/trainee_update.html", {"id": id})


def trainee_delete(request, id):
    return render(request, "trainee/trainee_delete.html", {"id": id})
