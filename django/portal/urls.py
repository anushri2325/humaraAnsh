from django.urls import include, path
from .views import ContactUsView, PatientSignUpView, SignUpView, DoctorSignUpView, PatientHomeView, DoctorHomeView, TeamView, login_success, login_request, contact_view

app_name = 'portal'

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    # path('signup/', SignUpView.as_view(), name='signup'),
    path('patient_sign_up/', PatientSignUpView.as_view(), name='patient_signup'),
    path('doctor_sign_up/', DoctorSignUpView.as_view(), name='doctor_signup'),
    path('doctor_home/', DoctorHomeView.as_view(), name='doctor_home'),
    path('patient_home/', PatientHomeView.as_view(), name='patient_home'),
    path('login_success/', login_success, name='login_success'),
    path('login/', login_request, name="login"),
    path('contact_us/', contact_view, name='Contact_Us'),
    path('team/', TeamView.as_view(), name='team'),
]