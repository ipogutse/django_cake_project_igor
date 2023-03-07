from django.test import TestCase
from .forms import RegistrationForm
from django.contrib.auth.models import User


# Create your tests here.
class RegistrationFormTestCase(TestCase):
    def test_form_fields(self):
        form_data = {'first_name': 'joey', 'last_name': 'django', 'username': 'joeyd',
                     'phone_number': '4162891436',
                     'email': 'joey@gmail.com', 'password1': 'Test@1234', 
                     'password2': 'Test@1234'}
        form = RegistrationForm(form_data)
        if form.errors:
            for field in form:
                for error in field.errors:
                    print(field, error)
        self.assertTrue(form.is_valid())
        
    def test_invalid_email(self):
        form_data = {'first_name': 'joey', 'last_name': 'django', 'username': 'joeyd',
                     'phone_number': '4162891436',
                     'email': 'joeygmail.com', 'password1': 'Test@1234', 
                     'password2': 'Test@1234'}
        form = RegistrationForm(form_data)
        if form.errors:
            for field in form:
                for error in field.errors:
                    print(field, error)
        self.assertFalse(form.is_valid())
        
    def test_username_exists(self):
        form_data = {'first_name': 'joyey', 'last_name': 'django', 'username': 'ipogutse',
                     'phone_number': '4162891436',
                     'email': 'joey@gmail.com', 'password1': 'Test@1234', 
                     'password2': 'Test@1234'}
        User.objects.create_user(username='ipogutse',email='joey@gmail.com',
                                        password='Test@1234',first_name='joyey',
                                        last_name='django')
        form = RegistrationForm(form_data)
        if form.errors:
            for field in form:
                for error in field.errors:
                    print(field, error)
        self.assertFalse(form.is_valid())
        
    def test_blank_field(self):
        form_data = {'first_name': 'joey', 'last_name': '', 'username': 'joeyd',
                     'phone_number': '4162891436',
                     'email': 'joey@gmail.com', 'password1': 'Test@1234', 
                     'password2': 'Test@1234'}
        form = RegistrationForm(form_data)
        if form.errors:
            for field in form:
                for error in field.errors:
                    print(field, error)
        self.assertFalse(form.is_valid())
        