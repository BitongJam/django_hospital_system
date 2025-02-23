from django import forms
from .models import Patient, Doctor

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'contact']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
        }

        def clean_name(self):
            name = self.cleaned_data.get('name')
            if not name:
                raise forms.ValidationError('Name is required.')
            return name

        def clean_age(self):
            age = self.cleaned_data.get('age')
            if not age or age <= 0:
                raise forms.ValidationError('Age must be a positive number.')
            return age
        
class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'speiclization', 'contact']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'speiclization': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
        }

        def clean_name(self):
            name = self.cleaned_data.get('name')
            if not name:
                raise forms.ValidationError('Name is required.')
            return name

        def clean_speiclization(self):
            speiclization = self.cleaned_data.get('speiclization')
            if not speiclization:
                raise forms.ValidationError('Speiclization is required.')
            return speiclization

        def clean_contact(self):
            contact = self.cleaned_data.get('contact')
            if not contact:
                raise forms.ValidationError('Contact is required.')
            return contact