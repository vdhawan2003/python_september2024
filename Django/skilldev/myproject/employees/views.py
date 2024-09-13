from django.shortcuts import render, get_object_or_404, redirect 
from django.http import HttpResponse 
from employees.models import Employee, Department 
from django.db.models import Avg 
 
# Create Department and Employee 
def create_employee(request): 
    hr_dept = Department.objects.get_or_create(name="Human Resources")[0] 
    it_dept = Department.objects.get_or_create(name="Information Technology")[0] 
    employee1 = Employee.objects.get_or_create(name="Keerthi", dept=hr_dept, job_title="CEO", salary=50000.00)[0] 
    employee2 = Employee.objects.get_or_create(name="Test", dept=it_dept, job_title="Software Engineer", salary=75000.00, bonus=5000.00)[0] 
    return HttpResponse("Employees created successfully!") 
 
# Read Employees and Departments 
def read_employees(request): 
    employees = Employee.objects.all() 
    employee_info = [ 
        f"Name: {employee.name}, Job Title: {employee.job_title}, Department: {employee.dept.name}" 
        for employee in employees 
    ] 
    return HttpResponse("<br>".join(employee_info))
# Update Employee's Department 
def update_employee_department(request, employee_name): 
    employee = get_object_or_404(Employee, name=employee_name) 
    it_dept = Department.objects.get(name="Information Technology") 
    employee.dept = it_dept 
    employee.save() 
    return HttpResponse(f"{employee_name}'s department updated successfully!") 
 
# Delete Employee 
def delete_employee(request, employee_name): 
    employe = get_object_or_404(Employee, name=employee_name) 
    employe.delete() 
    return HttpResponse(f"{employee_name} deleted successfully!") 
 
# ORM Query: Filter Employees by Department 
def filter_employees_by_department(request): 
    it_employees = Employee.objects.filter(dept__name="Information Technology") 
    employee_list = [employee.name for employee in it_employees] 
    return HttpResponse("<br>".join(employee_list)) 
 
# ORM Query: Calculate Average Salary for Job Title 
def average_salary(request): 
    avg_salary = Employee.objects.filter(job_title="HR Manager").aggregate(Avg('salary')) 
    return HttpResponse(f"Average Salary for HR Manager: {avg_salary['salary__avg']}") 
 
# ORM Query: Get Employees with a Salary Greater than $40,000 
def high_paid_employees(request):
    high_paid_employees = Employee.objects.filter(salary__gt=40000) 
    if high_paid_employees.exists(): 
        employee_info = [ 
            f'Employee Name: {employee.name}, Salary: {employee.salary}' 
            for employee in high_paid_employees 
        ] 
        return HttpResponse("<br>".join(employee_info)) 
    else: 
        return HttpResponse("No employees found with salary greater than 40,000.")