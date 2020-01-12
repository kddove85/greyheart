from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from datetime import datetime

from .models import Greyhound
from .models import GreyPhoto
from .models import BoardMember
from .models import Event
from .models import Tribute
from .forms import AdoptionForm


def index(request):
    grey_photos_dict = {}
    greys_list = Greyhound.objects.all().exclude(spotlight__exact='')
    for greyhound in greys_list:
        grey_photo_list = GreyPhoto.objects.all().filter(grey=greyhound.id)
        grey_photos_dict[greyhound.id] = grey_photo_list
    context = {'greys_list': greys_list, 'grey_photos': grey_photos_dict, 'title': None}
    return render(request, 'app/index.html', context)


def about_us(request):
    board_members_list = BoardMember.objects.all().order_by('position')
    context = {'board_members_list': board_members_list, 'title': 'About Us'}
    return render(request, 'app/about_us.html', context)


def available_greys(request):
    grey_photos_dict = {}
    available_greys_list = Greyhound.objects.all().filter(is_available=True)
    for greyhound in available_greys_list:
        grey_photo_list = GreyPhoto.objects.all().filter(grey=greyhound.id)
        grey_photos_dict[greyhound.id] = grey_photo_list
    context = {'available_greys_list': available_greys_list, 'grey_photos': grey_photos_dict, 'title': 'Available Greys'}
    return render(request, 'app/available_greys.html', context)


def events(request):
    events_list = Event.objects.all().filter(event_date__gte=datetime.today())

    for event in events_list:
        event.start_time = clean_time(event.start_time)
        event.end_time = clean_time(event.end_time)

    context = {'events_list': events_list, 'title': 'Events'}
    return render(request, 'app/events.html', context)


def clean_time(time_str):
    if time_str.startswith('0'):
        time_str = time_str[1:]
    return time_str


def get_adoption_form(request):
    greys_list = Greyhound.objects.all().exclude(spotlight__exact='')
    context = {'greys_list': greys_list}
    if request.method == 'POST':
        form = AdoptionForm(request.POST)
        if form.is_valid():
            try:
                subject = 'Greyheart Adoption Form'
                message = compose_message(form)
                send_mail(subject, message, 'greyheart.us@gmail.com', ['greyheart.us@gmail.com'], fail_silently=False)
                messages.add_message(request, messages.SUCCESS, f'Successfully submitted adoption form')
            except:
                messages.add_message(request, messages.ERROR, f'An error occurred while attempting to submit form')
            return index(request)
    else:
        form = AdoptionForm()
        return render(request, 'app/adopt.html', {'form': form, 'title': 'Adopt a Grey'})


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


def tributes(request):
    current_year = datetime.now().year
    tributes_list = Tribute.objects.filter(year_lost=current_year)
    possible_years = Tribute.objects.order_by('-year_lost').values('year_lost').distinct()

    tribute_list_for_view = []
    row_entries = []
    counter = 1
    row = 1

    for item in tributes_list:

        if counter % 3 == 1:
            row_entries.append(item)
        if counter % 3 == 2:
            row_entries.append(item)
        if counter % 3 == 0:
            row_entries.append(item)

        if len(row_entries) == 3:
            tribute_list_for_view.append(row_entries)
            row += 1

            row_entries = []

        counter += 1

    if len(row_entries) > 0:
        tribute_list_for_view.append(row_entries)

    context = {'tributes_list': tribute_list_for_view, 'current_year': current_year, 'all_years': possible_years,
               'title': 'Tributes'}
    return render(request, 'app/tributes.html', context)


def tributes_year_lost(request, year_lost):
    tributes_list = Tribute.objects.filter(year_lost=year_lost)
    possible_years = Tribute.objects.order_by('-year_lost').values('year_lost').distinct()

    tribute_list_for_view = []
    row_entries = []
    counter = 1
    row = 1

    for item in tributes_list:

        if counter % 3 == 1:
            row_entries.append(item)
        if counter % 3 == 2:
            row_entries.append(item)
        if counter % 3 == 0:
            row_entries.append(item)

        if len(row_entries) == 3:
            tribute_list_for_view.append(row_entries)
            row += 1

            row_entries = []

        counter += 1

    if len(row_entries) > 0:
        tribute_list_for_view.append(row_entries)

    context = {'tributes_list': tribute_list_for_view, 'current_year': year_lost, 'all_years': possible_years,
               'title': 'Tributes'}
    return render(request, 'app/tributes.html', context)
