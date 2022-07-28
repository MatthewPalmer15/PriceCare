from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from .models import User, SupportTicket, SupportTicketResponse

class CreateUser(UserCreationForm):
	""" Form for creating a new user """
	class Meta:
		model = User
		fields = [
			'username', 'email', 'password1', 'password2', 'profilepic']

	username	= forms.CharField(
					max_length=32,
					required=True,
					widget=forms.TextInput(
						attrs={
							'class': 'form-control form-resize mx-auto my-2',
							'placeholder': 'Username',
							'onkeyup': 'document.getElementById("reg_username").innerHTML = this.value'
						}
					)
				)
	email		= forms.EmailField(
					required=True,
					widget=forms.EmailInput(
						attrs={
							'class': 'form-control form-resize mx-auto my-2',
							'placeholder': 'Email'
						}
					)
				)
	password1	= forms.CharField(
					required=True,
					widget=forms.PasswordInput(
						attrs={
							'class': 'form-control form-resize mx-auto my-2',
							'placeholder': 'Password'
						}
					)
				)
	password2	= forms.CharField(
					max_length=64,
					required=True,
					widget=forms.PasswordInput(
						attrs={
							'class': 'form-control form-resize mx-auto my-2',
							'placeholder': 'Confirm Password'
						}
					)
				)
	profilepic	= forms.ImageField(
					widget=forms.FileInput(
						attrs={
							'class': 'form-control form-resize mx-auto my-2',
							'accept': 'image/jpeg, image/png',
							'onchange': 'read_image(this)'
							}
						)
					)
	agreement	= forms.BooleanField(
				required=True,
				widget=forms.CheckboxInput(
					attrs={
						'class': 'form-check-input mx-auto',
						'label': 'Agreement'
						}
					)
				)

	def __init__(self, *args, **kwargs) -> None:
		super(CreateUser, self).__init__(*args, **kwargs)
		self.fields['profilepic'].required = False

class EditUserDetails(UserChangeForm):
	""" Form for editing a user's details """
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'profilepic']

	username	= forms.CharField(
					max_length=32,
					required=True,
					widget=forms.TextInput(
						attrs={
							'class': 'form-control form-resize mx-auto my-2',
							'placeholder': 'Username',
							'onkeyup': 'document.getElementById("reg_username").innerHTML = this.value'
						}
					)
				)
	first_name	= forms.CharField(
					max_length=32,
					required=False,
					widget=forms.TextInput(
						attrs={
							'class': 'form-control form-resize mx-auto my-2',
							'placeholder': 'First Name'
						}
					)
				)
	last_name	= forms.CharField(
					max_length=32,
					required=False,
					widget=forms.TextInput(
						attrs={
							'class': 'form-control form-resize mx-auto my-2',
							'placeholder': 'Last Name'
						}
					)
				)
	email		= forms.EmailField(
					required=True,
					widget=forms.EmailInput(
						attrs={
							'class': 'form-control form-resize mx-auto my-2',
							'placeholder': 'Email'
						}
					)
				)
	profilepic	= forms.ImageField(
					widget=forms.FileInput(
						attrs={
							'class': 'form-control form-resize mx-auto my-2',
							'accept': 'image/jpeg, image/png',
							'onchange': 'read_image(this)'
						}
					)
				)

	def __init__(self, *args, **kwargs) -> None:
		super(EditUserDetails, self).__init__(*args, **kwargs)
		self.fields['profilepic'].required = False

class EditUserPassword(PasswordChangeForm):
	""" Form for editing a user's password """
	class Meta:
		model = User
		fields = ['old_password', 'new_password1', 'new_password2']

	old_password	= forms.CharField(
						required=True,
						widget=forms.PasswordInput(
							attrs={
								'class': 'form-control form-resize mx-auto my-2',
								'placeholder': 'Old Password'
							}
						)
					)
	new_password1	= forms.CharField(
						required=True,
						widget=forms.PasswordInput(
							attrs={
								'class': 'form-control form-resize mx-auto my-2',
								'placeholder': 'New Password'
							}
						)
					)
	new_password2	= forms.CharField(
						required=True,
						widget=forms.PasswordInput(
							attrs={
								'class': 'form-control form-resize mx-auto my-2',
								'placeholder': 'Confirm Password'
							}
						)
					)

class SupportTicketForm(forms.ModelForm):
	""" Form for creating a support ticket """
	class Meta:
		model = SupportTicket
		fields = ['subject', 'message', 'file']

	subject			= forms.CharField(
							max_length=64,
							widget=forms.TextInput(
								attrs={
									'class': 'form-control form-resize mx-auto my-2',
									'placeholder': 'Subject'
								}
							)
						)
	message			= forms.CharField(
							required=True,
							widget=forms.Textarea(
								attrs={
									'class': 'form-control form-resize mx-auto my-2',
									'placeholder': 'Message'
								}
							)
						)
	file			= forms.FileField(
							required=False,
							widget=forms.FileInput(
								attrs={
									'class': 'form-control form-resize mx-auto my-2',
									'accept': 'image/jpeg, image/png, application/pdf',
									'onchange': 'read_image(this)'
								}
							)
						)


class SupportTicketResponseForm(forms.ModelForm):
	""" Form for responding to a support ticket """
	class Meta:
		model = SupportTicketResponse
		fields = ['message', 'file']

	message			= forms.CharField(
						max_length=512,
						required=True,
						widget=forms.Textarea(
							attrs={
								'class': 'form-control mx-auto my-2',
								'placeholder': 'Enter Message'
							}
						)
					)
	file 			= forms.FileField(
						required=False,
						widget=forms.FileInput(
							attrs={
								'class': 'form-control mx-auto my-2',
								'accept': 'image/jpeg, image/png , application/pdf , application/msword , application/vnd.openxmlformats-officedocument.wordprocessingml.document',
							}
						)
					)
