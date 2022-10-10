from django.shortcuts import render, redirect
from .models import Emp
from .forms import EmpForm

# Create your views here.
def emp_list(request):
    emp = Emp.objects.all()
    context = {
        'emp': emp,
    }
    return render(request, 'emp/list.html', context)

def create_emp(request):
    form = EmpForm()
    if request.method == 'POST':
        form = EmpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emp_list')

    context = {
        'form': form,
    }
    return render(request, 'emp/create.html', context)

def edit_emp(request, pk):
    emp= Emp.objects.get(id=pk)
    form = EmpForm(instance=emp)

    if request.method == 'POST':
        form = EmpForm(request.POST, instance=emp)
        if form.is_valid():
            form.save()
            return redirect('empl_list')

    context = {
        'emp': emp,
        'form': form,
    }
    return render(request, 'emp/edit.html', context)



def delete_emp(request, pk):
    emp= Emp.objects.get(id=pk)

    if request.method == 'POST':
        emp.delete()
        return redirect('emp_list')

    context = {
        'emp': emp,
    }
    return render(request, 'emp/delete.html', context)
