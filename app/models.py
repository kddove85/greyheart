from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta
from cloudinary.models import CloudinaryField

start_date = datetime(2000, 1, 1, 0, 0, 0)
TIMES = []
for td in (start_date + timedelta(minutes=30 * it) for it in range(24)):
    TIMES.append((td.strftime("%I:%M"), td.strftime("%I:%M")))

HOURS = [(x, x) for x in range(1, 13)]
AM_PM = [('AM', 'AM'),
         ('PM', 'PM'),
         ]

USABLE_PHOTOS = [('media\event_photos\meet_n_greet.png', 'Meet & Greet')
                 ]


# Create your models here.
class Greyhound(models.Model):
    YES = 'YES'
    NO = 'NO'
    MAYBE = 'MAYBE'

    CHOICES = [
        (YES, 'Yes'),
        (NO, 'No'),
        (MAYBE, 'Maybe'),
    ]

    DOG_FRIENDLY_CHOICES = CHOICES
    CAT_FRIENDLY_CHOICES = CHOICES
    KID_FRIENDLY_CHOICES = CHOICES

    name = models.CharField(max_length=255)
    bio = models.TextField()
    is_available = models.BooleanField(default=False)

    is_dog_friendly = models.CharField(
        max_length=5,
        choices=DOG_FRIENDLY_CHOICES,
        default=YES,
    )

    is_cat_friendly = models.CharField(
        max_length=5,
        choices=CAT_FRIENDLY_CHOICES,
        default=YES,
    )

    is_kid_friendly = models.CharField(
        max_length=5,
        choices=KID_FRIENDLY_CHOICES,
        default=YES,
    )

    spotlight = models.TextField(blank=True, null=True)
    profile_image = CloudinaryField('image', blank=True, null=True)


class BoardMember(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    bio = models.TextField()
    profile_image = CloudinaryField('image', blank=True, null=True)


class Event(models.Model):
    name = models.CharField(max_length=255, null=True)
    event_date = models.DateField(null=True)
    start_time = models.CharField(choices=TIMES, default=1, max_length=10)
    start_am_pm = models.CharField(max_length=2, choices=AM_PM, default='AM', )
    end_time = models.CharField(choices=TIMES, default=1, max_length=10)
    end_am_pm = models.CharField(max_length=2, choices=AM_PM, default='AM',)
    host = models.CharField(max_length=255, null=True)
    address = models.TextField(null=True)
    photo = models.CharField(choices=USABLE_PHOTOS, max_length=255, null=True)

    def clean(self):
        time_format = '%I:%M %p'
        dt_start_time = datetime.strptime(f"{self.start_time} {self.start_am_pm}", time_format)
        dt_end_time = datetime.strptime(f"{self.end_time} {self.end_am_pm}", time_format)
        if dt_start_time > dt_end_time:
            raise ValidationError("Event cannot end before it begins!")
        return super().clean()


class Tribute(models.Model):
    pass
