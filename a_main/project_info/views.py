from django.shortcuts import render

# Create your views here.
def project_info(request):
    return render(request,'about_project.html')