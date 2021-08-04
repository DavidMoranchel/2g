from rest_framework import generics

# Serializers
from .serializers import (
    # Pet Owner serializers
    PetOwnerModelSerializer,
    PetOwnersListModelSerializer,
)

# Models
from .models import PetOwner, Pet


class PetOwnersListCreateAPIView(generics.ListCreateAPIView):

    queryset = PetOwner.objects.all()
    serializer_class = PetOwnersListModelSerializer

    def get_queryset(self):

        first_name_filter = self.request.GET.get("first_name")
        filters = {}
        if first_name_filter:
            filters["first_name__icontains"] = first_name_filter

        return self.queryset.filter(**filters)

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == "POST":
            serializer_class = PetOwnerModelSerializer

        return serializer_class
