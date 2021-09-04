from django.urls import include, path
from .views import PatientSignUpView, SignUpView, DoctorSignUpView, PatientHomeView, DoctorHomeView, login_success

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('patient_sign_up/', PatientSignUpView.as_view(), name='patient_signup'),
    path('doctor_sign_up/', DoctorSignUpView.as_view(), name='doctor_signup'),
    path('doctor_home/', DoctorHomeView.as_view(), name='doctor_home'),
    path('patient_home/', PatientHomeView.as_view(), name='patient_home'),
    path('login_success/', login_success, name='login_success'),
]