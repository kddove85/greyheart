from django.contrib import admin
from .models import Greyhound
from .models import GreyPhoto
from .models import BoardMember
from .models import Event
from .models import Tribute
from cloudinary import uploader


def delete_model(modeladmin, request, queryset):
    for obj in queryset:
        uploader.destroy(obj.profile_image.public_id)
        obj.delete()


# Register your models here.
class GreyhoundAdmin(admin.ModelAdmin):
    def get_actions(self, request):
        actions = super().get_actions(request)

        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    fields = ['name',
              'bio',
              'is_available',
              'is_dog_friendly',
              'is_cat_friendly',
              'is_kid_friendly',
              'spotlight',]
    list_display = ('name',)
    actions = [delete_model]


class GreyPhotoAdmin(admin.ModelAdmin):
    fields = ['grey',
              'profile_image']
    list_display = ('grey', 'profile_image')


class BoardMemberAdmin(admin.ModelAdmin):
    def get_actions(self, request):
        actions = super().get_actions(request)

        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    fields = ['name', 'title', 'position', 'bio', 'profile_image']
    list_display = ('name', 'title', 'position')

    actions = [delete_model]


class EventAdmin(admin.ModelAdmin):
    fields = ['name', 'event_date', 'start_time', 'start_am_pm', 'end_time', 'end_am_pm', 'host', 'address', 'photo']
    list_display = ('name', 'event_date', 'start_time', 'start_am_pm', 'end_time', 'end_am_pm', 'host')


class TributeAdmin(admin.ModelAdmin):
    fields = ['name', 'year_lost', 'profile_image']
    list_display = ('name', 'year_lost')


admin.site.register(Greyhound, GreyhoundAdmin)
admin.site.register(GreyPhoto, GreyPhotoAdmin)
admin.site.register(BoardMember, BoardMemberAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Tribute, TributeAdmin)
