from django import forms
from .models import ResourceList


class ResourceForm(forms.ModelForm):
    class Meta:
        model = ResourceList
        fields = ['title', 'description']  # to use all fields of a model use __all__ in a string.

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'})
        }
