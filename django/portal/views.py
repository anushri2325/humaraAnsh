from portal.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView, TemplateView

from .models import Patient
from .forms import PatientSignUpForm, DoctorSignUpForm
from .decorators import patient_required

class SignUpView(TemplateView):
    template_name = 'portal/signup.html'

class PatientSignUpView(CreateView):
    model = User
    form_class = PatientSignUpForm
    template_name = 'portal/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'patient'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('patient_home')

class DoctorSignUpView(CreateView):
    model = User
    form_class = DoctorSignUpForm
    template_name = 'portal/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'doctor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('doctor_home')

class PatientHomeView(TemplateView):
    template_name = 'portal/patient_home.html'

class DoctorHomeView(TemplateView):
    template_name = 'portal/doctor_home.html'

@login_required
def login_success(request):
    if request.user.is_doctor:
        return HttpResponseRedirect(reverse('doctor_home'))
    else:
        return HttpResponseRedirect(reverse('patient_home'))