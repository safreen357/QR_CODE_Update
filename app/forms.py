from dataclasses import fields
from django import forms
from matplotlib import widgets
#for modelform
from .models import RegistrationModel,AdminModel
from django.core import validators       

# class RegistrationForm(forms.Form):
#     fname=forms.CharField(min_length=3,max_length=25)
#     lname=forms.CharField(min_length=2,max_length=25)
#     email=forms.EmailField()
#     mobile=forms.IntegerField()
#     website=forms.CharField(max_length=75)
#     password=forms.CharField(widget=forms.PasswordInput)
#     confirm=forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(forms.ModelForm):
    class Meta:
        model=RegistrationModel
        fields=['fname','lname','email','mobile','website','password','confirm']
        labels={
            'fname':'First Name',
            'lname':'Last Name',
            'email':'Email',
            'mobile':'Mobile No.',
            'website':'Company Name',
            'password':'Password',
            'confirm':'Confirm Password',
            }
        help_text={'fname':{'First Name'}}
        error_messages={
            'fname':{'required':'Enter First Name Here'},
            'lname':{'required':'Enter Last Name Here'},
            'email':{'required':'Enter Email Here'},
            'mobile':{'required':'Enter Mobile Number Here'},
            'website':{'required':'Enter Company Website Here'},
            'password':{'required':'Enter Password Here'},
            'confirm':{'required':'Enter Confirm Password Here'},
            }

        widgets={
            'fname':forms.TextInput(attrs={'class':'form-control','placeholder':'First Name','required':True}),
            'lname':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control','placeholder':'Mobile'}),
            'website':forms.URLInput(attrs={'class':'form-control','placeholder':'Company Name'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),
            'confirm':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}),
            'date':forms.HiddenInput(attrs={'class':'form-control'}),
        }

class AdminForm(forms.ModelForm):
    class Meta:
        model=AdminModel
        fields=['name','password']
        labels={'name':'Name','password':'Password'}
        help_text={'name':{'Name'},'password':{'Password'}}
        error_messages={
            'name':{'required':'Enter Name',
            'password':{'required':'Enter Password'}}}
    
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Full Name'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),
        }