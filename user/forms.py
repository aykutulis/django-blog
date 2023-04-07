from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, min_length=3, label='Username')
    password = forms.CharField(
        max_length=20, min_length=3, label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(
        max_length=20, min_length=3, label='Confirm Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError('Passwords do not match')

        return {
            "username": cleaned_data.get('username'),
            "password": cleaned_data.get('password'),
        }


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, min_length=3, label='Username')
    password = forms.CharField(
        max_length=20, min_length=3, label='Password', widget=forms.PasswordInput)
