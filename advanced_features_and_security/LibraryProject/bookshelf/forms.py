# forms.py
from django.forms import ExampleForms

class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=100)
