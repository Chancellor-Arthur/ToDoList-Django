from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Todo
from authorization.models import Authorization
from .forms import TodoForm


def index(request):
    if not is_session(request):
        return redirect('index')
    todo_list = Todo.objects.filter(user_fk=request.session['user']).order_by('id')

    form = TodoForm()

    context = {'todo_list': todo_list, 'form': form}
    return render(request, 'todo/index.html', context)


@require_POST
def addTodo(request):
    if not is_session(request):
        return redirect('index')
    if not request.POST:
        return redirect('index')
    user = Authorization(user=request.session['user'])
    new_todo = Todo(text=request.POST['text'], user_fk=user)
    new_todo.save()
    return redirect('list')


def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('list')


def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()

    return redirect('list')


def deleteAll(request):
    Todo.objects.all().delete()

    return redirect('list')


def is_session(request):
    if request.session.get('user', None):
        if Authorization.objects.filter(user=request.session['user'], password=request.session['password']):
            return True
    return False


def deleteUser(request):
    del request.session['user']
    del request.session['password']
    return redirect('index')
