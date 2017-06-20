from django.contrib import admin
from .models import ClubTeam

# Register your models here.
# admin.site.register(ClubTeamAdmin)

class ClubTeamAdmin(admin.ModelAdmin):
	list_display = ('name', 'location')
admin.site.register(ClubTeam, ClubTeamAdmin)