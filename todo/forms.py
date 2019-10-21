from django import forms
from .models import Item

#inheriting forms from ModelForm
class ItemForm(forms.ModelForm):
    #inner class
    class Meta:
        model = Item
        fields = ('name', 'done')
