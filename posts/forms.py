from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Profile, upload_location

from django.core.files.images import get_image_dimensions
from django.contrib.auth import authenticate, get_user_model, login, logout

#third party lib
from pagedown.widgets import PagedownWidget
from material import *



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email has already been registered")
        return email


class PostForm(forms.ModelForm):
    class Meta:
        content = forms.CharField(widget=PagedownWidget)
        model = Post
        fields = [
            "title",
            "brief",
            "content",
        ]



class ProfileForm(forms.ModelForm):
    gender = forms.ChoiceField(choices= (
                                        (1, "MALE"),
                                        (2, "FEMALE"),
                                        (3, "OTHER"),
                                        )
    , widget= forms.RadioSelect)
    bio = forms.CharField(max_length=140)
    profilePic = forms.ImageField()

    #layout = Layout()

    class Meta:
        model = Profile
        fields = [
            "gender",
            "bio",
            "profilePic",
        ]

