from django import forms
from . models import moviemodel, commentmodel, registermodel2
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class addmovieform(forms.ModelForm):
    class Meta:
        model = moviemodel
        fields = '__all__'
        
    
class commentform(forms.ModelForm):
    class Meta:
        model = commentmodel
        fields = '__all__'
        widgets = {'movie':forms.HiddenInput, 'username': forms.HiddenInput ,'rating':forms.NumberInput(attrs={'max':5,'min':0}), 'comment':forms.Textarea(attrs={'placeholder':'Leave Your Comment Here.....','id':'cmtbox', 'class':'col-12'})}
        
    def clean_rating(self):
        cmt = self.cleaned_data['rating']
        if (cmt > 5) or (cmt <= 0):
            raise forms.ValidationError('Rating Must Be In (0.1 - 5.0)')
        return cmt
        
        
class registerform(UserCreationForm):   
    
    username = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))  
 
    class Meta:
        model=User
        fields=["username", "email", "password1", "password2"]
    
    
    def clean(self):
        return self.cleaned_data
        
    def clean_password2(self):
        pass2 = self.cleaned_data['password2']
        if len(pass2)<4:
            raise forms.ValidationError('error')
        return pass2
        
class registerform2(forms.ModelForm):
    
    username = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Example. John'}))
    ph_no = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Ph_No...'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Example. sample@gmail.com'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':' Confirm password'}))
    
    class Meta:
        model=registermodel2
        fields = ['username', 'email', 'ph_no', 'password', 'confirm_password']
        
    def clean_ph_no(self):
        data = self.cleaned_data["ph_no"]
        if len(str(data)) != 10:
            raise forms.ValidationError("Please Give A Valid 10 Digit Ph No.")
        
        if str(data)[0] not in ['9', '8', '7', '6']:
            raise forms.ValidationError("Please Give A Valid Ph No..")
        
        return data
    
        
    def clean_confirm_password(self):
        org_pass = self.cleaned_data.get('password')
        data = self.cleaned_data["confirm_password"]
        if org_pass != data:
            raise forms.ValidationError("Both Password Doesn't Match ! ")
        
        if len(data) < 4 :
            raise forms.ValidationError(" Password Must Contain Aleast 4 Char !")
        
        return data
    
    
        
    
class OTPForm(forms.Form):
    otp_token = forms.CharField(max_length=6, label='OTP')
    