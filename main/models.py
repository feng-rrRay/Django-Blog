from django.db import models

# Create your models here.

class myBlog(models.Model):
	myBlog_title = models.CharField(max_length=50)
	myBlog_author = models.CharField(max_length=50)
	myBlog_datetime = models.DateTimeField('Date Published')
	myBlog_content = models.TextField()

	def __str__(self):
		return self.myBlog_title
