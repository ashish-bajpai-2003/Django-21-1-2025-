from django import forms
from django.core import validators
class StudentRegistration(forms.Form):
    # name = forms.CharField(initial = "Ashish" , help_text = "name me keval ashish hi likhe ")
    # name = forms.CharField(label = 'Your name' , required =True , label_suffix = '' , initial = 'Swet' , disabled = True , help_text = 'limit 2 char')
    # name = forms.CharField(widget = forms.PasswordInput())
    # name = forms.CharField(widget = forms.URLInput())
    # name = forms.CharField(widget = forms.Textarea())
    # name = forms.CharField(widget = forms.HiddenInput())
    # name = forms.CharField(widget = forms.CheckboxInput())
    # name = forms.CharField(widget = forms.FileInput())
    # name = forms.CharField(widget = forms.TextInput(attrs = {'class' : 'Somecss1', 'id' : 'uniqueid'}))
    # name = forms.CharField(min_length= 4 , max_length= 10 , strip = False , empty_value='swet' ,
    #                         required = False, error_messages={'required' : 'Enter your name '})
    # def starts_with_s(value):
    #     if value[0] != 's':
    #         raise forms.ValidationError('Name should be starts with s .')
    # name = forms.CharField(validators = [starts_with_s])
    # error_css_class = 'error'
    # required_css_class = 'required'
    name = forms.CharField(error_messages={'required':'Enter Your name'})
    email = forms.EmailField(error_messages={'required' : "Enter Your email "})
    password = forms.CharField(widget = forms.PasswordInput , error_messages={'required' : "Enter Your password "})
    # repassword = forms.CharField(widget = forms.PasswordInput)
    # def clean(self):
    #     cleaned_data = super().clean()
    #     valpwd = self.cleaned_data['password']
    #     valrpwd = self.cleaned_data['repassword']
    #     if valpwd != valrpwd:
    #         raise forms.ValidationError('The paasword is not matched. ')
    # name = forms.CharField(validators = [validators.MaxLengthValidator(10)])

    # def clean(self):
    #     cleaned_data = super().clean()
    #     valname = self.cleaned_data['name']
    #     valemail = self.cleaned_data['email']
    #     if len(valname) < 4:
    #         raise forms.ValidationError("name should be more than 4 letters ")
        

    #     if len(valemail) <10:
    #         raise forms.ValidationError("email should be more than 10 . ")
    # password  = forms.CharField(widget = forms.PasswordInput())
    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) < 4:
    #         raise forms.ValidationError('enter name more than 4')
    #     return valname
    # email = forms.EmailField()
    # first_name = forms.CharField()
    # last_name = forms.CharField()
    # mobile = forms.IntegerField()
    # key = forms.CharField(widget = forms.HiddenInput())
    # roll = forms.IntegerField(min_value= 5)
    # price = forms.DecimalField(min_value=5 , max_digits=4 , decimal_places=1)
    # agree = forms.BooleanField(label_suffix = '', label = "I Agree")