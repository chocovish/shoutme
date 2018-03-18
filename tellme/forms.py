from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from .models import Comments,info


class SignupForm(UserCreationForm):   
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name',]
        #exclude = ["bio"]


class TestForm(forms.Form):
    ct = (('m', 'Male'), ('f', 'Female'))

    name = forms.CharField(min_length=3)
    age = forms.IntegerField(min_value=18)
    gender = forms.ChoiceField(choices=ct)
    photo = forms.FileField()


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']


class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

class ProfileUpdate2(forms.ModelForm):
    class Meta:
        model = info
        exclude = ["user"]