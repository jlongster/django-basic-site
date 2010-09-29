from django import forms
from django.contrib.auth.models import User
from models import UserProfile

class UserRegistrationForm(forms.Form):
    email = forms.EmailField()
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    def create_user():
        if not self.is_valid():
            return

        data = self.cleaned_data

        # First, make sure a user with this email doesn't already
        # exist
        if UserProfile.objects.filter(email__exact=data['email']).next():
            return False

        user = User.objects.create_user(username=data['email'],
                                        email=data['email'],
                                        password=data['password'])
        user.save()

        profile = UserProfile.objects.create(user=user,
                                             email=data['email'])
        profile.save()

        return user
