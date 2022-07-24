from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import User

class CreateUser(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2', 'profilepic']

	username 	= forms.CharField(
						max_length=32, 
						required=True, 
						widget=forms.TextInput(attrs={'class': 'form-control form-resize mx-auto my-2', 'placeholder': 'Username', 'onkeyup': 'document.getElementById("reg_username").innerHTML = this.value'})
						)
	email 	    = forms.EmailField(
						required=True, 
						widget=forms.EmailInput(attrs={'class': 'form-control form-resize mx-auto my-2', 'placeholder': 'Email'})
						)
	password1 	= forms.CharField(
						required=True, 
						widget=forms.PasswordInput(attrs={'class': 'form-control form-resize mx-auto my-2', 'placeholder': 'Password'})
						)
	password2	= forms.CharField(
						max_length=64,
						required=True, 
						widget=forms.PasswordInput(attrs={'class': 'form-control form-resize mx-auto my-2', 'placeholder': 'Confirm Password'})
						)
	profilepic 	= forms.ImageField(
					widget=forms.FileInput(attrs={'class': 'form-control form-resize mx-auto my-2', 'accept': 'image/jpeg, image/png', 'onchange': 'read_image(this)'})
					)

	def __init__(self, *args, **kwargs) -> None:
		super(CreateUser, self).__init__(*args, **kwargs)
		self.fields['profilepic'].required = False