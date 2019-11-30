from django.contrib import admin
from .models import Greyhound
from .models import BoardMember


# Register your models here.
class GreyhoundAdmin(admin.ModelAdmin):
    fields = ['name', 'bio', 'is_spotlight', 'profile_image']
    list_display = ('name',)


class BoardMemberAdmin(admin.ModelAdmin):
    fields = ['name', 'status', 'bio', 'profile_image']
    list_display = ('name',)


admin.site.register(Greyhound, GreyhoundAdmin)
admin.site.register(BoardMember, BoardMemberAdmin)
