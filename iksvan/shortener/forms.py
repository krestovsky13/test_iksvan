from django import forms
from django.contrib.auth.models import User

from .models import Urls


class SignUpForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'id': "inputUsername",
            'placeholder': "Username"})
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control mt-2",
            'id': "inputPassword",
            'placeholder': "Password"})
    )
    repeat_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control mt-2",
            'id': "ReInputPassword",
            'placeholder': "Repeat password"})
    )

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        password = cleaned_data['password']
        confirm_password = cleaned_data['repeat_password']

        if password != confirm_password:
            raise forms.ValidationError("Passwords don't match")

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )
        return user

    def clean_username(self):
        username = self.cleaned_data['username']

        if User.objects.filter(username=username).count() > 0:
            raise forms.ValidationError("A user with this name already exists")
        return username


class SignInForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'id': "inputUsername",
            'placeholder': "Username"})
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control mt-2",
            'id': "inputPassword",
            'placeholder': "Password"})
    )


class UrlForm(forms.ModelForm):
    class Meta:
        model = Urls
        fields = ('full_url',)
        widgets = {
            'full_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': "URL"
            }),
        }
