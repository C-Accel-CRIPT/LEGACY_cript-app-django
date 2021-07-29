from django import forms

# from .models import *


class MaterialForm(forms.Modelform):
    keywords = forms.ModelMultipleChoiceField(
        queryset=Keyword.objects,
        widget=forms.CheckboxSelectMultiple(),
        required=False,
    )
