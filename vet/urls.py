from django.urls import path

# Views
from .views import PetOwnersList, PetsList

urlpatterns = [
    path("owners/", PetOwnersList.as_view(), name="owners_list"),
    path("pets/", PetsList.as_view(), name="pets_list"),
]
