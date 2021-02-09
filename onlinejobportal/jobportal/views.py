from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,'home.html')

def latest_job(request):
    return render(request,'latest_job.html')