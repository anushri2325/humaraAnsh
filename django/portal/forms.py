from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.core.exceptions import ValidationError
from django.db.models import fields
from .models import Contact, Patient, User, Doctor

class PatientSignUpForm(UserCreationForm):
    pregnancy_month = forms.IntegerField(label = "Month of pregnancy")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
        'username',
        'email',
        'first_name' ,
        'last_name',
        'pregnancy_month',
        )
        
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_patient = True
        user.username = self.cleaned_data["username"]
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.save()
        patient = Patient.objects.create(user=user)
        patient.pregnancy_month = self.cleaned_data["pregnancy_month"]
        patient.save()
        return user

class DoctorSignUpForm(UserCreationForm):
    specialist = forms.CharField(label = "Specialist")
    hospital = forms.CharField(label = "Hospital")
    experience_years = forms.IntegerField(label = "Years of Experience")


    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','email','first_name' ,'last_name','specialist','hospital', 'experience_years')

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)

        user.username = self.cleaned_data["username"]
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name =self.cleaned_data["last_name"]
        user.is_doctor = True
        user.save()

        doctor = Doctor.objects.create(user=user)
        doctor.specialist = self.cleaned_data['specialist']
        doctor.hospital = self.cleaned_data['hospital']
        doctor.experience_years = self.cleaned_data['experience_years']
        doctor.save()
        return user

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
