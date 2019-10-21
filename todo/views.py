from django.shortcuts import render, HttpResponse, redirect
from .models import Item
from .forms import ItemForm

# Create your views here.
def get_todo_list(request):
    results = Item.objects.all()
    return render(request, "todo_list.html", {
        'items': results
    })
#django will return a dictionary, which is the form
def create_an_item(request):
    if request.method == "POST":
        #creating new form and inside constructor of form, populating with values from POST request item
        form = ItemForm(request.POST, request.FILES)
        #django will do automatic check that form is valid
        if form.is_valid():
            #form automatically knows form is valid and where to be saved, becaused of adding meta class
            form.save()
            return redirect(get_todo_list)
    else:
        form = ItemForm()

    return render(request, "item_form.html", {'form': form})
