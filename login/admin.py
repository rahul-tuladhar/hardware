from django.contrib import admin
from .models import Group, Profile

# Register your models here.
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'date')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'display_name', 'email')


admin.site.register(Group, GroupAdmin)
admin.site.register(Profile, ProfileAdmin)
