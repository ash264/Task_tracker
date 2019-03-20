from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm
from django.views.decorators.http import require_POST
# Create your views here.

def indexView(request):
    my_todo=Todo.objects.order_by('id')
    form=TodoForm()
    context={'my_todo': my_todo,'form':form}
    return render(request,'todo/index.html',context)

@require_POST

def addTodo(request):
    form=TodoForm(request.POST or None)
    if form.is_valid():
        req_new=Todo(text=form.cleaned_data['text'])
        req_new.save()
    return redirect('index')

def completedTodo(request,todo_id):
    obj=Todo.objects.get(pk=todo_id)
    obj.complete=True
    obj.save()
    return  redirect('index')

def deleteCompleted(request):
    obj= Todo.objects.filter(complete=True)
    obj.delete()
    return redirect('index')

def deleteAll(request):
    obj=Todo.objects.order_by('id')
    obj.delete()
    return redirect('index')
