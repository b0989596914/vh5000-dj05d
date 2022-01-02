from django.shortcuts import render
from .models import Person
from .forms import PersonModelForm
from django.http import request


def index(request):
    if request.method == "POST":
        form = PersonModelForm(request.POST)
        if form.is_valid():
            form.save()
            context = {'form':form}
            return render(request,"register/apply_success.html",context)
        else:
            return render(request,"register/apply_fail.html",context)
    form = PersonModelForm()
    context = {
        'form':form
    }
    
    return render(request, "register/apply.html", context)


def show_apply(request):
    person_list = Person.objects.all()
    context = {
        'person_list': person_list
    }
    return render(request, "register/show.html", context)