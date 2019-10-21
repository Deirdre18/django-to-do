from django.shortcuts import render, HttpResponse, redirect
from .models import Item

# Create your views here.
def get_todo_list(request):
    results = Item.objects.all()
    return render(request, "todo_list.html", {
        'items': results
    })
#django will return a dictionary, which is the form
def create_an_item(request):
    if request.method == "POST":
        new_item = Item()
        new_item.name = request.POST.get('name')
        #this is so that value for 'done' is saved to db
        new_item.done = 'done' in request.POST
        new_item.save()

        return redirect(get_todo_list)

    return render(request, "item_form.html")
