from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.core.exceptions import ValidationError
from .models import Patient, User

class PatientSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        # fields = '__all__'
        # labels = {
        #    'email' : '',
        #    'first_name' : '',
        #    'last_name' : '',
        #    'specialist' : '',
        #    'hospital' : '',
        #    'years of experience' : '',
        # }
        
        # widgets = {
		# 	'email':forms.TextInput(attrs={'class':'form-control','placeholder': 'email'}),
		# 	'first_name':forms.TextInput(attrs={'class':'form-control','placeholder': 'first name'}),
        #     'last_name':forms.TextInput(attrs={'class':'form-control','placeholder': 'last name'}),
        # }
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_patient = True
        user.save()
        patient = Patient.objects.create(user=user)
        # patient.email.add(*self.cleaned_data.get('email'))
        return user

class DoctorSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_doctor = True
        if commit:
            user.save()
        return user