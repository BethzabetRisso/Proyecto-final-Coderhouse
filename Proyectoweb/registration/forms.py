from .models import Profile as ProfileModel
from dataclasses import fields
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreationFormsWithEmail(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model  =User
        fields = ('username','email','password1','password2')

class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, max_length=200)
    class Meta:
        model = User
        fields = ['email']
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError(u'El email ya esta registrado. intenta con otro')
        return email

class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['avatar', 'bio', 'link']
        widgets  = {
            'avatar': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3' }),
            'bio': forms.Textarea(attrs={'class':'form-control-file mt-3', 'rows':3, 'placeholder': 'Biografia' }),
            'link': forms.URLInput(attrs={'class':'form-control-file mt-3', 'placeholder': 'Enlace' }),
       }



