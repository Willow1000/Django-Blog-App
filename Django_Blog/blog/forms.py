from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from django import forms
from .models import CustomUser


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}),required=True)
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(max_length=30, required=False, help_text='Required',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Second Name'}))
    class Meta:
        model = CustomUser
        fields = ['username','first_name','last_name','email','password1','password2']

    def __init__(self, *args,**kwargs):
        super(SignUpForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="text-muted">Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can’t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can’t be a commonly used password.</li><li>Your password can’t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted">Enter the same password as before, for verification.</span>'    
        

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Username"}))        
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"}))        
    class Meta:
        model = CustomUser