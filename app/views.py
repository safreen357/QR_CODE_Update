from audioop import mul
from django.shortcuts import redirect, render
from flask import render_template
from flask_bootstrap import Bootstrap
from requests import request
from resizeimage import resizeimage
import qrcode
from PIL import Image,ImageTk
from .forms import RegistrationForm,AdminForm
from .models import RegistrationModel,AdminModel
from django.http import HttpResponseRedirect
# for modelform
from django.db import IntegrityError
from datetime import date
# for filter 
from .filters import RegistrationFilter
# for pagination
from django.core.paginator import Paginator
# for search
from django.db.models import Q

def homepage(request):
    # # generating a QR code using the make() function  
    qr_img = qrcode.make("http://127.0.0.1:8000/qrcode") 
    # saving the image file  
    qr_img.save("homepage.jpg")
    if request.method == 'POST':
        print('post data')
        form = AdminForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            reg_save = AdminModel(name=name,password=password)
            reg_save.save()
            print('data saved into db ')
    else:
        form = AdminForm()
    return render(request,'homepage.html',{'form':form})

    

# Create your views here.
def registration(request):
    if request.method == 'POST':
        try:
            # print('post data')
            form = RegistrationForm(request.POST)
            if form.is_valid():
                fname = form.cleaned_data['fname']
                lname = form.cleaned_data['lname']
                email = form.cleaned_data['email']
                mobile = form.cleaned_data['mobile']
                website = form.cleaned_data['website']
                password = form.cleaned_data['password']
                confirm = form.cleaned_data['confirm']
                print('in try generate block executed')
                qr_data=(f"Employee id: {fname}\nEmployee name:{lname}\nemail:{email}\nmobile:{mobile}\nwebsite:{website}\npassword:{password}\nconfirm:{confirm}")
                qr_code = qrcode.make(qr_data)
                # print(qr_code)
                qr_code=resizeimage.resize_cover(qr_code,[180,180])
                qr_name = fname.lower()+"_"+lname.lower()
                qr_code.save("image/media/"+str(qr_name)+'.jpg')
                print('### image saved')
                img = "image/media/"+str(qr_name)+'.jpg'
                print('### img ',img)
                print('QR Code Generated Successfully')
                today = date.today()
                current_date= today.strftime("%b-%d-%Y")
                # print("current_date =", current_date)
                reg_save = RegistrationModel(fname=fname,lname=lname,email=email,mobile=mobile,website=website,password=password,confirm=confirm,image=img,date=current_date)
                reg_save.save()
                print('data saved into db ')
                id = RegistrationModel.objects.all().last()
                user = fname.capitalize() + " "+ lname.capitalize()
                context ={
                    'form':form,
                    'id':id,
                    'user':user}
                return render(request,"split_index.html",context)
            else:
                context = {'form':form,}
                return render(request,"split_index.html",context)
        except IntegrityError as e:
            print('except block')
            e = 'user available in db'
            context = {
                'form':form,
                'e':e}
    else:    
        print("get block executed")
        form = RegistrationForm()   # get emtpy form
        context = {'form':form}
        print('context ',context)
        print('context type ',type(context))
    return render(request,"split_index.html",context)

    # return img 
def fun_image(request):
    # get q name from search box
    if 'q' in request.GET:
        q=request.GET['q']
        print('q ',q)
        # search in multiple columns
        multiple_q = Q(Q(fname__contains=q) | Q(lname__contains=q) | Q(email__contains=q) | Q(mobile__contains=q) | Q(website__contains=q))
        print('mul q ',multiple_q)
        userlist=RegistrationModel.objects.filter(multiple_q)
    else:
        userlist = RegistrationModel.objects.all()
        # for pagination
        paginator=Paginator(userlist,6)
        page_number=request.GET.get('page')
        userlist=paginator.get_page(page_number)
    context = {
        'userlist':userlist,
        
    }
    return render(request,'userlist.html',context)

def qr_code(request):
    return render(request,"qrcode.html")