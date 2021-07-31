from django.urls import path

# Views
from .views import PetOwnersListCreate, PetsList

urlpatterns = [
    path("owners/", PetOwnersListCreate.as_view(), name="owners_list"),
    path("pets/", PetsList.as_view(), name="pets_list"),
]
