# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

from .models import Todo

# Create your views here.


def index(request):
    todos = Todo.objects.order_by().reverse().all()

    return render(request, 'index.html', {"todos": todos})


def addTodo(request):
    if request.method == "GET":
        return redirect("/")

    else:
        title = request.POST.get("title")
        newTodo = Todo(title = title, completed = False)
        

        newTodo.save()

        return redirect("/")
 


def update(request,id):
   todo = Todo.objects.filter(id=id).first()

   todo.completed = not todo.completed

   todo.save()

   return redirect("/")

   
def updateTodo(request,id):
   todo = Todo.objects.filter(id=id).first()

   title = request.POST.get("title")

   todo.title= title

   todo.save()

   return redirect("/")





def delete(request,id):
   todo = Todo.objects.filter(id=id).first()
   
   todo.delete()

   return redirect("/")



