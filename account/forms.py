from django import forms
from account.models import *
from account.models import *

# Customer Creation Form
class CustomerForm(forms.Form):
    class Meta:
        models = Coustomer
        fields = ['username' , 'email' , 'password' , 'confirm_password']


        def clean_password(self):
            password = self.cleaned_data.get('password')
            confirm_password = self.data['confirm_password']
            if password != confirm_password:
                raise forms.ValidationError('Passwords do not match')
            return password
        


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        fields = [ 'first_name', 'last_name', 'email_second',  'phone' , 'phone_second' , 'address',]

    


       
class VendorRequestForm(forms.ModelForm):
    class Meta:
        model = VendorApply
        fields = '__all__'
