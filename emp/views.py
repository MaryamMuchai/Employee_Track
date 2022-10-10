from django.shortcuts import render

# Create your views here.
def emp_list(request):
    return render(request, 'emp/list.html')

def create_emp(request):
    return render(request, 'emp/create.html')

def edit_emp(request, pk):
    return render(request, 'emp/edit.html')

def delete_emp(request, pk):
    return render(request, 'emp/delete.html')