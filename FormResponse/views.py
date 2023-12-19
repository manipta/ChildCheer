from django.shortcuts import render
from form.models import formresponse
def FormResponse(request):
    data=formresponse.objects.all()
    context={'title':"Form Responses",
             'data': data
             }
    print(data)
    return render(request,'formresponse/index.html',context)
