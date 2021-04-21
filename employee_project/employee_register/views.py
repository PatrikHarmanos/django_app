from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee


def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "employee_register/employee_list.html", context)


def employee_form(request, id=0):
    # if method is GET
    if request.method == "GET":
        # if id is 0, than we have insert operation
        if id == 0:
            form = EmployeeForm()
        # update operation
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)

        return render(request, "employee_register/employee_form.html", {'form': form})
    # if method is POST
    else:
        # if we insert
        if id == 0:
            form = EmployeeForm(request.POST)
        # if we update
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid():
            form.save()
        return redirect('/employee/list')


def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')
