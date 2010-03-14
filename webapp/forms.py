from django import forms
from django.contrib.auth.models import User
from app.model import lists
from webapp.account.models import Account


class AccountForm(forms.Form):

    email = forms.EmailField(max_length=75)
    username = forms.CharField(max_length=30)
    password = forms.CharField(label=(u'Password'),
                               widget=forms.PasswordInput(render_value=False)) 
    repassword = forms.CharField(label=(u'Password'),
                               widget=forms.PasswordInput(render_value=False)) 


    def clean_password(self):
        if self.cleaned_data['password'] == self.data['repassword']:
            return self.cleaned_data['password']
        else:
            raise forms.ValidationError("The passwords you entered in don't match.")


    def clean_username(self):

        username = self.cleaned_data['username']

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None

        if user:
            raise forms.ValidationError("This username is already taken.")
        else:
            return username

        
    def clean_email(self):

        email = self.cleaned_data['email']

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None

        try:
            account = Account.objects.get(pk=email)
        except Account.DoesNotExist:
            account = None

        if account or user:
            raise forms.ValidationError("An account for this email address has already been created.")
        else:
            return email


class ListForm(forms.Form):

    listname = forms.CharField(max_length=30)

    def clean_username(self):

        name = self.cleaned_data['listname']
        
        #todo: check for validity of name, (must be a valid email address, e.g. length can't exceed 64 characters)
        return name

