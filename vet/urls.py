from django.urls import path

# Views
from .views import (
    # Pet owners
    PetOwnersListCreateAPIView,
)

urlpatterns = [
    # Pet owners
    path("owners/", PetOwnersListCreateAPIView.as_view(), name="owners_list-create"),
    # path(
    #     "owners/<int:pk>",
    #     PetOwnerRetrieveUpdateDestroyAPIView.as_view(),
    #     name="owners_retrieve-update-destroy",
    # ),
]
