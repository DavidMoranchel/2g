from django.urls import path

# Views
from .views import (
    # Pet owners
    PetOwnersListCreateAPIView,
    PetOwnersRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    # Pet owners
    path("owners/", PetOwnersListCreateAPIView.as_view(), name="owners_list-create"),
    path(
        "owners/<int:pk>",
        PetOwnersRetrieveUpdateDestroyAPIView.as_view(),
        name="owners_retrieve-update-destroy",
    ),
]
