# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages

from django.shortcuts import render,redirect,HttpResponse
from .models import Courses

# Create your views here.
def index(request):
    course = Courses.objects.all()
    # print course
    return render(request,"courses_app/index.html",{'course':course})

def add(request):
    errors = Courses.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
           messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        c = Courses.objects.create(name=request.POST['name'], desc=request.POST['desc'])
        c.save()
        return redirect('/')

def delete(request, id):
    cour= Courses.objects.get(id=id)
    cour.delete()
    return redirect('/')

def confirmation(request, id):
    cour = Courses.objects.get(id=id)
    print '*'*50
    print cour.name
    return render(request, 'courses_app/delete.html', {'course':cour})