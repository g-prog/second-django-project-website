from django import forms
from .models import Registrationdata, loginn


class Registrationform(forms.Form):
    username = forms.CharField(max_length=100,
                                    widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    password = forms.CharField(max_length=100, 
                widget=forms.PasswordInput(attrs={
                    'class':'form-control',
                    'placeholder':'Username'
                }))

                                 
    email = forms.CharField(max_length=100,
                            widget=forms.EmailInput(attrs={
                                'class':'form-control',
                                'placeholder':'Email'
                            }))

    phone = forms.CharField(max_length=100,
                        widget=forms.NumberInput(attrs={
                            'class':'form-control',
                            'placeholder':'Phone'
                        }))

class RegistrationModal(forms.ModelForm):
    class Meta:
        model = Registrationdata
        fields = [

            
            'username',
            'password',
            'email',
            'phone'
        ]


        widgets = {
            'username':forms.TextInput(attrs={
                    'class':'form-control',
                    'placeholder':'Username'
                }),
                
  
                'password':forms.PasswordInput(attrs={
                    'class':'form-control',
                    'placeholder':'Password'
                }),

                'email':forms.EmailInput(attrs={
                    'class':'form-control',
                    'placeholder':'Email'
                }),

                'phone':forms.NumberInput(attrs={
                    'class':'form-control',
                    'placeholder':'Phone'
                }),

                



            
        }

class loginnModal(forms.ModelForm):
    class Meta:
        model = loginn
        fields = [
            'username',
            'password',
        ]
        widgets = {'username':forms.TextInput(attrs={
                    'class':'form-control',
                    'placeholder':'Username'
                }),
                
  
                'password':forms.PasswordInput(attrs={
                    'class':'form-control',
                    'placeholder':'Password'
                }),

        }