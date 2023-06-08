from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Todo
from .forms import TodoForm
from django.views.decorators.csrf import csrf_protect

# Create your views here.

def index(request):
    todoapp = Todo.objects.all()
    # give a list of what_do for each element of the list
    todo_titles = ", " .join([x.title for x in todoapp])
    context: dict[str, Any] =  {"todoapp": todoapp,
                                "todo_titles": todo_titles,
                                "stats": {
                                    "done": 1,
                                    "to_do": 2,
                                    "to_do_deleted": 5,
                                    "total": len(todoapp),
                                }
                                }
    #return HttpResponse("Le cose da fare sono: " + todo_titles + ".")
    return render(request,"todos/index.html", context)


@csrf_protect
def details(request, todo_id):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/todoapp/")
    else:
        todo = get_object_or_404(Todo, pk = todo_id)
        form = TodoForm(instance = todo)
        context: dict[str, Any] =  {"todo": todo,
                                    "form": form,
                                    }
        return render(request,"todos/details.html", context)