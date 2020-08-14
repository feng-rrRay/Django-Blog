from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class myBlog(models.Model):
	myBlog_title = models.CharField(max_length=50)
	myBlog_author = models.ForeignKey(User, on_delete=models.CASCADE)
	myBlog_datetime = models.DateTimeField('Date Published')
	myBlog_content = models.TextField()

	def __str__(self):
		return self.myBlog_title

class comment(models.Model):
	"""docstring for comment"""
	comment_article = models.ForeignKey(myBlog, on_delete=models.CASCADE)
	comment_author = models.ForeignKey(User, on_delete=models.CASCADE)
	comment_datetime = models.DateTimeField('Date Published')
	comment_content = models.CharField(max_length=200)

	def __str__(self):
		return self.comment_content
		