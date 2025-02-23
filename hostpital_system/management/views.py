from django.shortcuts import render, redirect,get_object_or_404
from .models import Patient, Doctor
from .forms import PatientForm

# Create your views here.
def home(request):
    return render(request, 'management/home.html')

def patients(request):
    patients = Patient.objects.all()
    return render(request, 'management/patients.html', {'patients': patients})

def doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'management/doctors.html', {'doctors': doctors})


def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patients')
        else:
            return render(request, 'management/add_patient.html', {'form': form})

    return render(request, 'management/add_patient.html')

def edit_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patients')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'management/edit_patient.html', {'form': form, 'patient': patient})

def delete_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('patients')
    return render(request, 'management/delete_patient.html', {'patient': patient})