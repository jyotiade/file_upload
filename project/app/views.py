from django.shortcuts import render

from .models import Student
from .forms import StudentForm

def  home(request):
    form=StudentForm()
    msg="registration form"
    if request.method=="POST":
        form=StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            msg="sucessfully registered"
        else:
            msg="please fill again"
    
    return render(request,'home.html',{'form':form,'msg':msg})

def show(request):
    data1=Student.objects.all()
    data=data1.values()
    return render(request,'show.html',{'data':data})