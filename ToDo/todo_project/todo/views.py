from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem

def todoView(request):
    all_todo_items = TodoItem.objects.all()
    print(type(all_todo_items))
    return render(request, 'todo.html', {'all_items':all_todo_items})

def addTodo(request):
    new_item = TodoItem(content = request.POST['content'], status = "Not Completed")

    new_item.save()
    return HttpResponseRedirect('/todo/')

def deleteTodo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id = todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')

def updateTodo(request, todo_id):
    all_items = TodoItem.objects.all()
    return render(request,'update.html', {'all_items':all_items, 'e_id':todo_id })

def crossoff(request, todo_id):
    obj = TodoItem.objects.get(id=todo_id)
    obj.status = "Completed"
    obj.save()
    return HttpResponseRedirect('/todo/')


def editTodo(request, todo_id):
    new_content = request.POST['content']
    obj = TodoItem.objects.get(id = todo_id)
    obj.content = new_content
    obj.save()
    return HttpResponseRedirect('/todo/')