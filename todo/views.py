from django.shortcuts import render, redirect, get_object_or_404
from .models import Item  #imports the Item db
from .forms import ItemForm  # imports or custom django form


# Create your views here.
def get_todo_list(request):
    # 'query set' puts all the items in the db ino a variable
    items = Item.objects.all()
    # Dict with all our items in it, and added as an argument to the
    # render request
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    # if POST i.e a new todo item is added, user returned to get_todo_list.html
    # if GET they get the add_item.html
    # 2 new variables are set to get the forms inputs
    # because done is a checkbox, we are looking for 'done' in request.POST
    # then create a new item ( and give it our new variables )
    if request.method == 'POST':
        form = ItemForm(request.POST)  # defines the form
        if form.is_valid():  # tells Django to compare the submitted data with what is required on the form
            form.save()  # saves the form
            return redirect('get_todo_list')


    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)


def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id) # gets the item with an id = to that was passed into the view via the url, if nothing there gives a 404
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)  #defines the form
        if form.is_valid():  #tells Django to compare the submitted data with what is required on the form
            form.save()  #saves the form
            return redirect('get_todo_list')

    form = ItemForm(instance=item)  #instance=item prefills the form with the info from the database
    context = {
        'form': form
    }
    return render(request, 'todo/edit_item.html', context)


def toggle_item(request, item_id):
    item = get_object_or_404(Item, id=item_id) # gets the item with an id = to that was passed into the view via the url, if nothing there gives a 404
    item.done = not item.done 
    item.save()
    return redirect('get_todo_list')


def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id) # gets the item with an id = to that was passed into the view via the url, if nothing there gives a 404
    item.delete()
    return redirect('get_todo_list')
