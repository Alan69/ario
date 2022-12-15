from django.contrib import admin
from .models import Request, RequestTypeTwo, RequestTypeThree
# Register your models here.
admin.site.register(Request)
admin.site.register(RequestTypeTwo)
admin.site.register(RequestTypeThree)