from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# class RegistrationForm(UserCreationForm):
#     first_name = forms.CharField(max_length=30, required=True, help_text='Username is required.')    
#     last_name = forms.CharField(max_length=30, required=False)
#     email = forms.EmailField(max_length=30, required=True, help_text='email is required.')
#     phone_number = forms.CharField(max_length=10, required=True)
    
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email', 'phone_number']
        
#     def clean_phone_number(self):
#         phone_number = self.cleaned_data.get('phone_number')
#         if len(phone_number) != 10:
#             raise forms.ValidationError('Enter valid 10 dogit phone number')
#         return phone_number
    
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Enter a valid email address')
    first_name = forms.CharField(required=True, max_length=50)
    last_name = forms.CharField(required=True, max_length=50)
    phone_number = forms.CharField(required=True, max_length=10)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'phone_number')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number.isdigit():
            raise ValidationError("Phone number should contain only digits")
        return phone_number

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.phone_number = self.cleaned_data['phone_number']
        
        if commit:
            user.save()
        return user

            