from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ["username", "email", "password1", "password2"]

	def save(self, commit=True):
		usr = super(NewUserForm, self).save(commit=False)
		usr.email = self.cleaned_data['email']
		if commit:
			usr.save()
		return usr