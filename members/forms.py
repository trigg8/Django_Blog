from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=100)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=100)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=100)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=100)
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=100)
    #last_login = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=100)
    is_superuser = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check'}),max_length=100)
    is_staff = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check'}),max_length=100)
    is_active = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check'}),max_length=100)
    #date_joined = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=100)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'is_superuser', 'is_staff', 'is_active',)
