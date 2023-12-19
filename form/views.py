from django.shortcuts import render
from .models import formresponse
from django.contrib import messages
from django.http import HttpResponse
def form(request):
    context={'title':'Form Page'}
    if request.method=='POST':
        name=request.POST['name'].capitalize()
        prof=request.POST['prof'].capitalize()
        city=request.POST['city'].capitalize()
        country=request.POST['country'].capitalize()
        contact=request.POST['contact']
        remarks=request.POST['remarks']
        voluntAs=request.POST['voluntAs']
        new_entry=formresponse(name=name,profession=prof,city=city,country=country,contact=contact,remarks=remarks,volas=voluntAs)
        if len(name) and len(prof) and len(city) and len(country) and len(contact)==10:
            new_entry.save()
            messages.success(request,"Response Submitted!")
        elif len(name)==0:
            messages.error(request,"Failed! Enter Valid Name")
        elif len(prof)==0:
            messages.error(request,"Failed! Enter a Valid Profession")
        elif len(city)==0:
            messages.error(request,"Failed! Enter Valid City")
        elif len(country)==0:
            messages.error(request,"Failed! Enter Valid Country")
        elif ~(contact==10):
            messages.error(request,"Failed! Enter Valid Contact Details")
        else:
            messages.error(request,"Failed! Response Not Submitted")
    return render(request,'form/index.html',context)
