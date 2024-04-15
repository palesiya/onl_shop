from django import forms
from home.models import Email


class EmailForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        widget=forms.TextInput(
            attrs={"id": "email", "class": "form-control" "active", "placeholder": "Your email...", "autocomplete": "on"}
        )
    )

    def save(self, commit=True):
        data = self.cleaned_data
        email_f = Email(**data)
        if commit:
            return email_f.save()
        return email_f
