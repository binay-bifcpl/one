from django import forms
from .models import Requisition

class RequisitionForm(forms.ModelForm):
    class Meta:
        model = Requisition
        fields = ['name', 'quantity', 'date', 'image']
