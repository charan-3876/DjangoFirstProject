from django.shortcuts import render
from . models import NewJobs,Rdetails,Alog
# Create your views here.
def Home(request):
    return render(request,'home.html')

def latest_job(request):
    newjobs = NewJobs.objects.all()
    data = {
        'newjobs':newjobs
    }
    return render(request,'latest_job.html',data)

def userlogin(request):
    return render(request,'userlogin.html')

def recruiterlogin(request):
    rdetails = Rdetails.objects.all()
    data = {
        'rdetails':rdetails
    }
    return render(request,'recruiterlogin.html',data)

def adminlogin(request):
    alog = Alog.objects.all()
    data = {
        'alog':alog
    }
    return render(request,'adminlogin.html',data)

def contact(request):
    return render(request,'contact.html')

