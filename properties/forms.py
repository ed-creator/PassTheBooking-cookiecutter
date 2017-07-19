from django.forms import ModelForm
from . import Property

class PropertyForm(ModelForm):
    class Meta
        model = Article
        fields = ['address_line_one','address','no_of_bedroom','sq_feet']

        
