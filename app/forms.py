from django import forms
from app.constants import States
from app.constants import OccupationTime
from app.constants import ActivityLevel
from app.constants import Involvement
from app.constants import YesNo
from app.constants import Dwelling
from app.constants import OwnRent
from app.constants import YesNoNA
from app.constants import Occupants


class AdoptionForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=50)
    last_name = forms.CharField(label='Last Name', max_length=50)
    email = forms.CharField(label='Email', max_length=100)
    phone_number = forms.CharField(label='Phone Number', max_length=100)
    occupation = forms.CharField(label='Occupation', max_length=100)
    street = forms.CharField(label='Street', max_length=100)
    city = forms.CharField(label='City', max_length=100)
    state = forms.ChoiceField(label='State', choices=[(s['alpha'], s['name']) for s in States.states])
    zip = forms.CharField(label='Zip Code', max_length=5)
    occupant_time = forms.ChoiceField(label='How long have you lived here?',
                                      choices=[(ot['alpha'], ot['name']) for ot in OccupationTime.occupation_time])
    activity_level = forms.ChoiceField(label='What is the activity level of your household?',
                                       choices=[(al['alpha'], al['name']) for al in ActivityLevel.activity_level])
    involvement = forms.ChoiceField(label='Are you interested in adopting or fostering?',
                                    choices=[(i['alpha'], i['name']) for i in Involvement.involvement])
    other_pets = forms.ChoiceField(label='Do you have other pets?',
                                   choices=[(i['alpha'], i['name']) for i in YesNo.yes_no])
    dwelling = forms.ChoiceField(label='Please select your type of dwelling',
                                 choices=[(i['alpha'], i['name']) for i in Dwelling.dwelling])
    rent_or_own = forms.ChoiceField(label='Do you rent or own your dwelling?',
                                    choices=[(i['alpha'], i['name']) for i in OwnRent.own_or_rent])
    permission = forms.ChoiceField(label='Do you have permission from the landlord or condo association to have a dog?',
                                   choices=[(i['alpha'], i['name']) for i in YesNoNA.yes_no_na])
    occupants = forms.ChoiceField(label='How many people live in your household?',
                                  choices=[(i['alpha'], i['name']) for i in Occupants.number_of_occupants])
    awareness = forms.ChoiceField(label='Are all of the adults in your household aware of this adoption/foster and '
                                        'agree to it?',
                                  choices=[(i['alpha'], i['name']) for i in YesNo.yes_no])
