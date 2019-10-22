from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
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
        #django will do automatic check that form is valid. Server side form validation
        if form.is_valid():
            #form automatically knows form is valid and where to be saved, becaused of adding meta class
            form.save()
            return redirect(get_todo_list)
    else:
        form = ItemForm()

    return render(request, "item_form.html", {'form': form})

#creating new instance of item. Want to get object from the item table, specifically primary key
def edit_an_item(request, id):

    item = get_object_or_404(Item, pk=id)

    if request.method == "POST":

        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(get_todo_list)
    else:
        form = ItemForm(instance=item)
    return render(request, "item_form.html", {'form': form})

def toggle_status(request, id):
    item = get_object_or_404(Item, pk=id)
    item.done = not item.done
    item.save()
    return redirect(get_todo_list)
