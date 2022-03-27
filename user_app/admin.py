from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class PhoneAdmin(admin.ModelAdmin):
    pass
    # list_display = ('id', 'name', 'price', 'image', 'release_date', 'lte_exists', 'slug')
