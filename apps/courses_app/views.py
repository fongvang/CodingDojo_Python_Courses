from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *

# Create your views here.
def index(request):
    context = { "courses" : courses.objects.all() }
    return render(request, 'index.html', context)

# def new(request):
def new(request):
    errors = courses.objects.basic_validator(request.POST)
    # check if the errors object has anything in it
    if len(errors):
    # if the errors object contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
    # redirect the user back to the form to fix the errors
            return redirect('/')
    else:
        courses.objects.create(
            name = request.POST['name'],
            description = request.POST['description']
        )
        return redirect('/')

def remove(request, id):
    query = courses.objects.get(id=id)
    return render(request, "remove.html", {"query": query})


def destroy(request, id):
    course = courses.objects.get(id=id)
    print(course)
    course.delete()
    return redirect('/')