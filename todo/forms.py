from django import forms  # gives us access to the django forms functionality
from .models import Item  # imports our Item model


class ItemForm(forms.ModelForm):  # our class which inherits
                                  # funcionality from forms.ModelForm
    class Meta:  # inner class to set the parameters for the form
        model = Item  # references our db
        fields = ['name', 'done']  # tells it the fields we want to display
