from django.contrib import admin
from .models import book
from .models import author_info
# Register your models here.
admin.site.register(book)
admin.site.register(author_info)