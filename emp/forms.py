from django import forms
from django.forms import ModelForm
from .models import Emp

class EmpForm(ModelForm):
    class Meta:
        model = Emp
        
        fields = ('emp_name', 'emp_dept', 'emp_salary','date_join','emp_address')

        widgets = {
            'emp_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'emp_dept': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Role'}),
            'emp_salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Salary'}),
            'date_join': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date Joined'}),
            'emp_address': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),

        }