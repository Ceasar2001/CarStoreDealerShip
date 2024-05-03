from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class EditProfileForm(UserChangeForm):
    password = forms.CharField(label='New Password', widget=forms.PasswordInput, required=False)
    confirm_password = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

class NewOfferForm(forms.Form):
    CATEGORIES = (
        (1, "Cars"),
        (2, "Atv"),
        (3, "Scooter"),
        (4, "Automobile"),
    )

    name = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField(decimal_places=2, widget=forms.NumberInput)
    category = forms.ChoiceField(choices=CATEGORIES, widget=forms.RadioSelect)
    image = forms.ImageField()


class EditOfferForm(forms.Form):
    CATEGORIES = (
        (1, "Cars"),
        (2, "Atv"),
        (3, "Scooter"),
        (4, "Automobile"),
    )

    name = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField(decimal_places=2, widget=forms.NumberInput)
    category = forms.ChoiceField(choices=CATEGORIES, widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        item = kwargs.pop("item", None)
        super(EditOfferForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['description'].required = False
        self.fields['price'].required = False
        self.fields['category'].required = False
        

        if item:
            self.fields["name"].widget.attrs["placeholder"] = item.name
            self.fields["description"].widget.attrs["placeholder"] = item.description
            self.fields["price"].widget.attrs["placeholder"] = item.price 

