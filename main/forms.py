from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import comment, myBlog
from ckeditor.widgets import CKEditorWidget

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


class CommentForm(forms.Form):
	"""docstring for CommentForm"""
	comment_content = forms.CharField(label='友善的评论是交流的起点', max_length=150)

	class Meta:
		model = comment
		fields = ("comment_content")

class EditForm(forms.Form):
	myBlog_title = forms.CharField(label='请输入标题', max_length=50)
	myBlog_content = forms.CharField(widget=CKEditorWidget())

	class Meta:
		model = myBlog
		fields = ("myBlog_title", "myBlog_content")
	
		