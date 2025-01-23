from django.shortcuts import render
from . forms import StudentRegistration
# Create your views here.
def showformdata(request):
    fm = StudentRegistration(auto_id= "custom_%s", label_suffix = '--')
    fm.order_fields(field_order = ['first_name' , 'last_name' , 'name' , 'email'])
    return render(request , 'enroll/userregistration.html',{'form' : fm})
