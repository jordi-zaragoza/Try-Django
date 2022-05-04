from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label="",
                            widget=forms.TextInput(attrs={"placeholder": "Title"}))
    email = forms.EmailField()
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Description",
                "class": "new-class-name two",
                "rows": 20,
                "cols": 50
            })
    )
    price = forms.DecimalField(initial="199.99")

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'email'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "CFE" in title:
            raise forms.ValidationError("This is not a valid title")
        if "news" in title:
            raise forms.ValidationError("This is not a valid title")
        return title

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if email.endswith(".es"):
            raise forms.ValidationError("Do not end with .es")
        return email


class RawProductForm(forms.Form):
    title = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": "Title"}))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Description",
                "class": "new-class-name two",
                "rows": 20,
                "cols": 50
            })
    )
    price = forms.DecimalField(initial="199.99")
