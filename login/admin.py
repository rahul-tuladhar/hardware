from django.contrib import admin
from .models import Group, User

# Register your models here.
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'date')


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'display_name', 'email', 'affiliations')


admin.site.register(Group, GroupAdmin)
admin.site.register(User, UserAdmin)
