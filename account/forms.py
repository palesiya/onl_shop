from django import forms
from account.models import User


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", 'password')
        widgets = {
            'password': forms.PasswordInput()
        }

    def clean(self):
        try:
            user = User.objects.get(username=self.cleaned_data.get('username'))
        except User.DoesNotExist:
            self.add_error('username', 'Invalid username')
            raise forms.ValidationError("Invalid username")
        if not user.check_password(self.cleaned_data.get('password')):
            self.add_error('password', 'Invalid password')
            raise forms.ValidationError("Invalid password")
        self.cleaned_data.update(user=user)
        return self.cleaned_data


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
