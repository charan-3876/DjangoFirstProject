from django.shortcuts import render

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
