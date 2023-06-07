from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm

# Create your views here.

def index(request):
    todoapp = Todo.objects.all()
    # give a list of what_do for each element of the list
    todo_titles = ", " .join([x.title for x in todoapp])
    context = {
        "todos": todoapp,
    }
    #return HttpResponse("Le cose da fare sono: " + todo_titles + ".")
    return render(request,"todos/index.html", context)

def details(request, todo_id):
    todo = get_object_or_404(Todo, pk = todo_id)
    form = TodoForm(instance = todo)
    context: dict[str, Any] =  {"todo": todo,
                                 "form": form,
                                }
    return render(request,"todos/details.html", context)