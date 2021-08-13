from django.shortcuts import render, redirect
import datetime
# Create your views here.
from django.http import HttpResponse
from myapp.models import  MyModel
from myapp.forms import MyForm
from django.contrib import messages


def my_form(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/show")
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)
    else:
        form = MyForm()
    return render(request, 'index.html', {'form': form})


def show(request):
    md = MyModel.objects.all()
    return render(request, "show.html", {'md': md})


def edit(request, id):
    md = MyModel.objects.get(id=id)
    print("in edit")
    return render(request, 'edit.html', {'md': md})


def update(request, id):
    md = MyModel.objects.get(id=id)
    print("in update")
    form = MyForm(request.POST, instance=md)
    if form.is_valid():
        form.save()
        print("shhowing")
        return redirect("/show")
    print("not valid from")
    return render(request, 'edit.html', {'md': md})


def delete(request, id):
    md = MyModel.objects.get(id=id)
    md.delete()
    return redirect("/show")