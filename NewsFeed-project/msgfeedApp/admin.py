from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Person)
#admin.site.register(Tag)
admin.site.register(Message)
admin.site.register(Comment)
admin.site.register(Like)