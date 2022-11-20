from django.shortcuts import render, redirect
from .models import Emp
from .forms import EmpForm, NewUserForm
from django.contrib import messages

from django.contrib.auth.forms import AuthenticationForm
# UserCreationForm
from django.contrib.auth import login, authenticate

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
            return redirect('emp_list')

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


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("emp_list")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="register/login.html", context={"login_form":form})
