from django.urls import path

# Views
from .views import (
    # Pet owners
    PetOwnersListAPIView,
    # PetOwnersListCreateAPIView,
    # PetOwnerRetrieveUpdateDestroyAPIView,
    # Pets
    # PetsListCreateAPIView,
)

urlpatterns = [
    # Pet owners
    path("owners/", PetOwnersListAPIView.as_view(), name="owners_list")
    # path("owners/", PetOwnersListCreateAPIView.as_view(), name="owners_list-create"),
    # path(
    #     "owners/<int:pk>",
    #     PetOwnerRetrieveUpdateDestroyAPIView.as_view(),
    #     name="owners_retrieve-update-destroy",
    # ),
    # Pets
    # path("pets/", PetsListCreateAPIView.as_view(), name="pets_list"),
]
