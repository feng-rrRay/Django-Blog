from django.shortcuts import render, redirect
from .models import myBlog, comment
from .forms import NewUserForm, CommentForm
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.utils import timezone
# Create your views here.

def homepage(request):
	return render(request = request,
				  template_name = "main/home.html",
				  context = {"myBlogs":myBlog.objects.all})

def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f"Your Account Created:{username}")
			login(request, user)
			messages.success(request, f"You are now registered as {username}")
			return redirect("/")
		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg}: {form.error_messages}")


	form = NewUserForm
	return render(request,
				  "main/register.html",
				  context={"form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "Logged out successfully")
	return redirect("main:homepage")

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}")
				return redirect("main:homepage")
			else:
				messages.error(request, 'Invalid Username or password')
		else:
			messages.error(request, 'Invalid Username or password')

	form = AuthenticationForm()

	return render(request, 
				  "main/login.html",
				  {"form":form})

def detail(request, myBlog_id):
	blog = myBlog.objects.get(pk=myBlog_id)
	commentset = comment.objects.filter(comment_article=blog)
	if request.method == 'POST':
        # create a form instance and populate it with data from the request:
		form = CommentForm(request.POST)
        # check whether it's valid:
		if form.is_valid():
			if request.user.is_authenticated:
	            # process the data in form.cleaned_data as required
				new_comment = comment(comment_content=form.cleaned_data.get('comment_content'),
	            					  comment_article=blog, 
	            					  comment_datetime=timezone.now(),
	            					  comment_author=request.user)
				new_comment.save()
			else:
				messages.info(request, '请先登录/注册再进行评论')
				return redirect("/login")
            # ...
            # redirect to a new URL:
			form = CommentForm()
			

    # if a GET (or any other method) we'll create a blank form
	else:
		form = CommentForm()
	return render(request = request,
				  template_name = "main/detail.html",
				  context = {"blog":blog, "commentset":commentset, "form":form})





