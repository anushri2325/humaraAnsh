from django import forms
from django.core.exceptions import ValidationError
from portal.models import Doctor, Patient
from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'doctor', 'patient','body','file')
		
		widgets = {
			'title':forms.TextInput(attrs={'class':'form-control','placeholder': 'Title'}),
			'doctor':forms.TextInput(attrs={'class':'form-control','value':'', 'id': 'sanya', 'type':'hidden'}),
			'body':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Details'}),	
        }

	# def __init__(self, *args, **kwargs):
	# 	super().__init__(*args, **kwargs)
	# 	self.fields['patient'].queryset = Patient.objects.none()



