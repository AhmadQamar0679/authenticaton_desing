from django.shortcuts import render

# Create your views here.
def add_patient(request):
    if request.method=='POST':
        data=request.POST
        patient_name=data.get('patient_name')
        

    return render(request,'add_patient.html')



