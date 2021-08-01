from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from .models import Todo

# Create your views here.
def list_request(request):
    #temp = {'todo_list' : Todo.objects.all()}
    temp = {'todo_list' :Todo.objects.filter(is_delete = 0)}
    return render(request,'todomain/todomain.html',temp)

def insert(request:HttpRequest):
    content = request.POST['content']
    print(content)
    is_delete = 0
    status = 1
    todo = Todo(content = content,is_delete=is_delete,status = status)
    todo.save()
    return redirect('/')

def delete(request,todo_id):
    Todo.objects.filter(id = todo_id).update(is_delete = 1)
    return redirect('/')


def update(request,todo_id):
    print("LOOOK HEREEEE")
    temp = Todo.objects.get(id = todo_id)
    if temp.status==True:
        Todo.objects.filter(id = todo_id).update(status = False)
    else:
        Todo.objects.filter(id = todo_id).update(status = True)
    return redirect('/')