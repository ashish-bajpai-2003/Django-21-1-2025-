from django.shortcuts import render
# from django.http import HttpResponseRedirect
from . forms import StudentRegistration
from .models import Student
# Create your views here.
# def thankyou(request):
#     return render(request , 'enroll/success.html')

def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            # print("Form validated. ")
            # print('name' , fm.cleaned_data['name'])
            # print('Email' , fm.cleaned_data['email'])
            # print('Password' , fm.cleaned_data['password'])
            # print('Repassword' , fm.cleaned_data['repassword'])
            # print('Password', fm.cleaned_data['password'])
            # print('roll' , fm.cleaned_data['roll'])
            # print('Price' , fm.cleaned_data['price'])
            # print('Agree' , fm.cleaned_data['agree'])

            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = Student(name = nm ,email = em , password = pw )
            reg.save()
            # name = fm.cleaned_data['name']
            # print("email " , fm.cleaned_data['email'])
            # print('password ' , fm.cleaned_data['password'])
            # return HttpResponseRedirect('/regi/success')
            # return render(request , 'enroll/success.html', {'nm' : name})
           
    # fm = StudentRegistration(initial = {'name' : 'Ashish'})
    else:
        fm = StudentRegistration()
        print("This is from get request ")
    return render(request , 'enroll/userregistration.html',{'form' : fm})
