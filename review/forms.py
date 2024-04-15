from django import forms
from review.models import Review


class ReviewForm(forms.Form):
    name = forms.CharField(
        label="Name",
        widget=forms.TextInput(
            attrs={"id": "name", "class": "form-control" "active", "placeholder": "Your name...", "autocomplete": "on"}
        )
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.TextInput(
            attrs={"id": "email", "class": "form-control" "active", "placeholder": "Your email...", "autocomplete": "on"}
        )
    )
    product_name = forms.CharField(
        label="Product_name",
        widget=forms.TextInput(
            attrs={"id": "product_name", "class": "form-control" "active", "placeholder": "product_name...", "autocomplete": "on"}
        )
    )
    review = forms.CharField(
        label="Review",
        widget=forms.Textarea(
            attrs={"id": "review", "class": "form-control" "active", "placeholder": "Your review...", "autocomplete": "on"}
        )
    )

    def save(self, commit=True):
        data = self.cleaned_data
        msg = Review(**data)
        if commit:
            return msg.save()
        return msg
