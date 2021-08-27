from django.urls import include, path
from .views import PatientSignUpView

urlpatterns = [
    path('parent_sign_up', PatientSignUpView, name='parent_sign_up'),
]