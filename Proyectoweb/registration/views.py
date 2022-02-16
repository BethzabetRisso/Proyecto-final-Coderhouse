from atexit import register
from unicodedata import name
from venv import create
from django.shortcuts import render
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .models import Profile 
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, UserCreationFormsWithEmail, EmailForm


class SignUpView(CreateView):
    form_class = UserCreationFormsWithEmail
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'



def get_form(self, form_class=None):
    form = super(SignUpView, self).get_form()
    form.fields('username').widget = forms.TextInput (attrs={'class':'form-control mb-2', 'placeholder': 'Nombre de usuario'}) 
    form.fields('email').widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder': 'Email'})
    form.fields('password1').widget = forms.PasswordInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Contraseña'  })
    form.fields('password2').widget = forms.PasswordInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Repita la contraseña'  })
    form.fields('username').label = 'test'
    form.fields('email').label = ''
    form.fields('password1').label = ''
    form.fields('password2').label = ''
    form.fields('username')
    return form

@method_decorator(login_required, name = 'dispatch')
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    model = Profile
    
    def get_object(self):
        try: 
            return Profile.objects.get(user = self.request.user)
        except Profile.DoesNotExist:
            return Profile.objects.create(user = self.request.user)


@method_decorator(login_required, name = 'dispatch')
class EmailUpdate(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user

def get_form(self, form_class = None):
    form = super(EmailUpdate, self).get_form()
    form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder': 'Email'})
    return form