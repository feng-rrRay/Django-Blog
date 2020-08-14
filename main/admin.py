from django.contrib import admin
from .models import myBlog, comment
# Register your models here.

admin.site.register(myBlog)

admin.site.register(comment)