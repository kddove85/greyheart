from django import forms


class AdoptionForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.CharField(label='Email', max_length=100)
    phone_number = forms.CharField(label='Phone Number', max_length=100)
    occupation = forms.CharField(label='Occupation', max_length=100)
    street = forms.CharField(label='Street', max_length=100)
    city = forms.CharField(label='City', max_length=100)
    state = forms.CharField(label='State', max_length=100)
    zip = forms.CharField(label='Zip Code', max_length=100)
