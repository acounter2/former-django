from django.shortcuts import render,redirect
from . forms import Teacher_Form

def teacher_create(request):
     if request.method=="POST":
        form=Teacher_Form(request.POST)
        if form.is_valid():
           form.save()

           return redirect("teacher:teacher_create")

     else:
           form=Teacher_Form()
     return render(request,"form.html",{"form":form})