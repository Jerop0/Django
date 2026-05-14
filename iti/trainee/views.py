from django.shortcuts import render, redirect
from django.views import View, generic
from django.urls import reverse_lazy
from .models import Trainee
from .forms import TraineeForm, TraineeFormModel
from course.models import Course


class TraineeList(generic.ListView):
    queryset = Trainee.objects.filter(is_active=True)
    template_name = 'trainee/trainee_list.html'
    context_object_name = "students"


def trainee_details(request, id):
    trainee = Trainee.objects.get(pk=id)
    return render(request, "trainee/trainee_details.html", {"trainee": trainee})


class TraineeAdd(View):
    def get(self, request):
        context = {"students": Trainee.objects.all(), 'form': TraineeFormModel()}
        return render(request, "trainee/trainee_add.html", context)

    def post(self, request):
        form = TraineeFormModel(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Trainee_List')
        return render(request, 'trainee/trainee_add.html', {'form': form, 'errors': form.errors})


class TraineeAddGeneric(generic.CreateView):
    model = Trainee
    template_name = 'trainee/trainee_add.html'
    context_object_name = 'trainee'
    form_class = TraineeFormModel
    success_url = reverse_lazy('Trainee_List')


def trainee_add_form(request):
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
    trainee = Trainee.objects.get(pk=id)
    form = TraineeFormModel(instance=trainee)
    if request.method == "POST":
        form = TraineeFormModel(data=request.POST, files=request.FILES, instance=trainee)
        if form.is_valid():
            form.save()
            return redirect("Trainee_Details", id=id)
    context = {"form": form, "id": id}
    return render(request, "trainee/trainee_update.html", context)


def trainee_delete(request, id):
    trainee = Trainee.objects.get(pk=id)
    if request.method == "POST":
        trainee.delete()
        return redirect("Trainee_List")
    context = {"trainee": trainee}
    return render(request, "trainee/trainee_delete.html", context)


def trainee_soft_delete(request, id):
    trainee = Trainee.objects.get(pk=id)
    trainee.is_active = False
    trainee.save()
    return redirect("Trainee_List")
