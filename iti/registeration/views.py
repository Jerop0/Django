from django.shortcuts import render


def registeration(request):
    return render(request, "registeration/registeration.html")


def registeration_login(request):
    return render(request, "registeration/registeration_login.html")


def registeration_signup(request):
    return render(request, "registeration/registeration_signup.html")
