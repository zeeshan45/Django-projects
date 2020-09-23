from django.shortcuts import render,redirect
from .forms import CngForm 
from .models import Cngmodel
from django.conf import settings
from django.contrib.auth.decorators import login_required
import requests
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

# Create your views here.

def index(request):
    return render(request,"index.html")

def viewcetificate(request):
    title=""
    if request.method == 'POST':
        title = request.POST.get('search')
    cngmodels = Cngmodel.objects.all()
    for cngmodel in cngmodels:
        if cngmodel.vehicle_no == title:
           
            permanent_exp_per = cngmodel.permanent_expen / cngmodel.total_expen*100
            permanent_exp_per = round(permanent_exp_per,2)
            if permanent_exp_per < 10:
                result = 'Pass'
            else:
                result = 'Fail'    
            arg = {
                'cng':cngmodel,
                'permanent_exp_per':permanent_exp_per,
                'result':result

            }
            return render(request, "formoutput.html",arg)
        else:
            messages.info(request,'NOT FOUND')
    return render(request,"viewcertificate.html") 


def formoutput(request):
    return render(request, "formoutput.html")
    
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'kwkcenter' and password == 'kwkcenter@123':
            return redirect('createcertificate')           
    return render(request,"login.html")

def createcertificate(request):
    form = CngForm()
    
    if request.method == 'POST':
        form = CngForm(request.POST or None)
        license_no = request.POST.get('license_no')
        report_no = request.POST.get('report_no')
        customer_name = request.POST.get('customer_name')
        vehicle_no = request.POST.get('vehicle_no')
        test_date = request.POST.get('test_date')
        test_due_date = request.POST.get('test_due_date')
        vehicle_type = request.POST.get('vehicle_type')
        fuel_type = request.POST.get('fuel_type')
        cylinder_no = request.POST.get('cylinder_no')
        cylinder_make = request.POST.get('cylinder_make')
        cylinder_spec = request.POST.get('cylinder_spec')
        last_testing_date = request.POST.get('last_testing_date')
        manufacturing_date = request.POST.get('manufacturing_date')
        longitude = request.POST.get('longitude')
        latitude = request.POST.get('latitude')
        valve_inspection = request.POST.get('valve_inspection')
        visual_inspection = request.POST.get('visual_inspection')
        cylinder_threading = request.POST.get('cylinder_threading')
        internal_inspection = request.POST.get('internal_inspection')
        plate_no = request.POST.get('plate_no')
        as_pr_making = request.POST.get('as_pr_making')
        actual_wt = request.POST.get('actual_wt')
        loss_wt = request.POST.get('loss_wt')

        diff_wt = request.POST.get('diff_wt')

        wall_thick_min = request.POST.get('wall_thick_min')
        wall_thick_max = request.POST.get('wall_thick_max')
        vol_cap = request.POST.get('vol_cap')
        working_press = request.POST.get('working_press')
        testing_press = request.POST.get('testing_press')
        total_expen = request.POST.get('total_expen')
        permanent_expen = request.POST.get('permanent_expen')
        image = request.FILES.get('image')
        if form.is_valid():
            cngmodel = Cngmodel(license_no=license_no,report_no=report_no,customer_name=customer_name,diff_wt=diff_wt,
            vehicle_no=vehicle_no,test_date=test_date,test_due_date=test_due_date,vehicle_type=vehicle_type,cylinder_spec=cylinder_spec,
            fuel_type=fuel_type,cylinder_no=cylinder_no,cylinder_make=cylinder_make,last_testing_date=last_testing_date,image=image,
            manufacturing_date=manufacturing_date,longitude=longitude,cylinder_threading=cylinder_threading,permanent_expen=permanent_expen,
            latitude=latitude,valve_inspection=valve_inspection,visual_inspection=visual_inspection,internal_inspection=internal_inspection,
            plate_no=plate_no,as_pr_making=as_pr_making,actual_wt=actual_wt,wall_thick_min=wall_thick_min,loss_wt=loss_wt,
            wall_thick_max=wall_thick_max,vol_cap=vol_cap,working_press=working_press,testing_press=testing_press,total_expen=total_expen)
            cngmodel.save()
            print("successfull")
            alert = "Create Successfully"
            return render(request,"createcertificate.html",{'alert_mess':alert}) 
        else:
            alert = "Something missing!"
            print(form.errors) 
            return render(request,"createcertificate.html") 
            #print(cngmodel)  
            #print(manufacturing_date)
            #print(vol_cap)
            #print(test_date)
            #pass\
            
    return render(request,"createcertificate.html")  


def success(request):
     return HttpResponse('successfuly uploaded') 

