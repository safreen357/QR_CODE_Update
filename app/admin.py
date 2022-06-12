from django.contrib import admin
from .models import RegistrationModel
# Register your models here.

@admin.register(RegistrationModel)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['id','fname','lname','email','mobile','website','password','confirm','image','date']

