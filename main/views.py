from django.shortcuts import render, HttpResponse,redirect
from .models import ToDo


def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list":todo_list})


def second(request):
    return HttpResponse("test 2 page")

def third(request):
    return HttpResponse("This is page test3")

def dz311(request):
    return render(request, "dz311.html")

def dz312(request):
    return render(request, "dz312.html")

def dz313(request):
    return render(request, "dz313.html")

def add_todo(request):
    form = request.POST
    text = form["todo_text"] 
    todo = ToDo(text=text)
    todo.save()
    return redirect(test) 


def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favourite = True
    todo.save()
    return redirect(test)

def unmark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favourite = False
    todo.save()
    return redirect(test)

def close_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_closed = not todo.is_closed
    todo.save()
    return redirect(test)

