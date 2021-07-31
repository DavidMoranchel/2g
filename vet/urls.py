from django.urls import path

# Views
from .views import PetOwnersListCreate, PetsList, PetOwnerDetailAPIView

urlpatterns = [
    path("owners/", PetOwnersListCreate.as_view(), name="owners_list"),
    path("owners/<int:pk>", PetOwnerDetailAPIView.as_view(), name="owners_detail"),
    path("pets/", PetsList.as_view(), name="pets_list"),
]
