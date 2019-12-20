from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.contrib import messages
from django.core.mail import send_mail

from .models import Greyhound
from .models import BoardMember
from .forms import AdoptionForm


def index(request):
    greys_list = Greyhound.objects.all().filter(is_spotlight=True)
    context = {'greys_list': greys_list}
    return render(request, 'app/index.html', context)


def about_us(request):
    board_members_list = BoardMember.objects.all()
    context = {'board_members_list': board_members_list}
    return render(request, 'app/about_us.html', context)


def available_greys(request):
    available_greys_list = Greyhound.objects.all().filter(is_available=True)
    context = {'available_greys_list': available_greys_list}
    return render(request, 'app/available_greys.html', context)


def get_adoption_form(request):
    greys_list = Greyhound.objects.all().filter(is_spotlight=True)
    context = {'greys_list': greys_list}
    if request.method == 'POST':
        form = AdoptionForm(request.POST)
        if form.is_valid():
            try:
                subject = 'Greyheart Adoption Form'
                message = 'Greyheart Adoption Form goes Here'
                message = compose_message(form)
                send_mail(subject, message, 'greyheart.us@gmail.com', ['greyheart.us@gmail.com'], fail_silently=False)
                messages.add_message(request, messages.SUCCESS, f'Successfully submitted adoption form')
            except:
                messages.add_message(request, messages.ERROR, f'An error occurred while attempting to submit form')
            return render(request, 'app/index.html', context)
    else:
        form = AdoptionForm()
        return render(request, 'app/adopt.html', {'form': form})


def compose_message(form):
    strings = [f"Name: {form.data['first_name']} {form.data['last_name']}", f"Email: {form.data['email']}",
               f"Phone Number: {form.data['phone_number']}", f"Occupation: {form.data['occupation']}",
               f"Are you interested in adopting or fostering: {form.data['involvement']}", 'Address',
               form.data['street'], f"{form.data['city']}, {form.data['state']}", f"{form.data['zip']}",
               f"How long have you lived here? {form.data['occupant_time']}",
               f"What is the activity level at your household? {form.data['activity_level']}",
               f"Please select your type of dwelling: {form.data['dwelling']}",
               f"Do you rent or own your dwelling? {form.data['rent_or_own']}",
               f"Do you have other pets? {form.data['other_pets']}",
               f"Do you have permission from the landlord or condo association to have a dog? {form.data['permission']}",
               f"How many people live in your household? {form.data['permission']}",
               f"Are all of the adults in your household aware of this adoption/foster and agree to it? {form.data['awareness']}"]
    return "\n".join(strings)
