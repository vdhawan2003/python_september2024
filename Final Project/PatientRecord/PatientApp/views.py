from django.shortcuts import render, redirect
from .models import Patient

#List all patients
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient_list.html', {'patients':patients})

#Create new patient
def patient_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        disease = request.POST['disease']
        admission_date = request.POST['admission_date']
        Patient.objects.create(name=name, age=age, disease=disease, admission_date=admission_date)
        return redirect('patient_list')
    return render(request,'patient_form.html')

#Update an existing patient
def patient_update(request, id):
    patient = Patient.objects.get(id=id)
    if request.method == 'POST':
        patient.name  = request.POST['name']
        patient.age = request.POST['age']
        patient.disease = request.POST['disease']
        patient.admission_date = request.POST['admission_date']
        patient.save()
        return redirect('patient_list')
    return render(request,'patient_form.html', {'patient': patient})

#Delete a patient
def patient_delete(request, id):
    patient = Patient.objects.get(id=id)
    patient.delete()
    return redirect('patient_list')


