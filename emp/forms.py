from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import Emp

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class EmpForm(ModelForm):
    Departments= (
        ('1','IT'),
        ('2','Accounts'),
        ('3','HR'),
        ('4','Procurement'),
    )
    emp_dept = forms.ChoiceField(choices=Departments)

    class Meta:
        model = Emp
        fields = ('emp_name', 'emp_dept', 'emp_salary','date_join','emp_address')

    widgets = {
        'emp_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
        'emp_salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Salary'}),
        'date_join': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date Joined'}),
        'emp_address': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),

        }

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model: User
        fields = ["name","username", "email", "number", "password1","password2"]

    def save (self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            return user