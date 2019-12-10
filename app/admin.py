from django.contrib import admin
from .models import Greyhound
from .models import BoardMember
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
              'is_spotlight',
              'profile_image']
    list_display = ('name',)
    actions = [delete_model]


class BoardMemberAdmin(admin.ModelAdmin):
    def get_actions(self, request):
        actions = super().get_actions(request)

        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    fields = ['name', 'title', 'bio', 'profile_image']
    list_display = ('name',)

    actions = [delete_model]


admin.site.register(Greyhound, GreyhoundAdmin)
admin.site.register(BoardMember, BoardMemberAdmin)
