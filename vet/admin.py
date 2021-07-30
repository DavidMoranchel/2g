from django.contrib import admin

from .models import Pet, PetOwner

admin.site.register(Pet)
admin.site.register(PetOwner)
