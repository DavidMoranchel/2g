from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend


# Serializers
from .serializers import (
    # Pet Owner serializers
    PetOwnerModelSerializer,
    PetOwnersListModelSerializer,
    # Pet serializers
    PetModelSerializer,
    PetListModelSerializer,
    # Pet dates serializers
    PetDateModelSerializer,
    PetDateListModelSerializer,
    PetDatePetRetrieveModelSerializer,
    PetDatePartialUpdateModelSerializer,
)

# Models
from .models import PetOwner, Pet, PetDate


class PetOwnersListCreateAPIView(generics.ListCreateAPIView):

    queryset = PetOwner.objects.all()
    serializer_class = PetOwnersListModelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["first_name", "=last_name"]
    # filterset_fields = ["first_name", "last_name"]

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == "POST":
            serializer_class = PetOwnerModelSerializer

        return serializer_class


class PetOwnersDatesListCreateAPIView(generics.ListCreateAPIView):

    queryset = PetDate.objects.all()
    serializer_class = PetDateListModelSerializer

    def get_queryset(self):
        owner_id = self.kwargs["pk"]
        filters = {}
        if owner_id:
            filters["pet__owner_id"] = owner_id

        return self.queryset.filter(**filters)


class PetOwnersRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = PetOwner.objects.all()
    serializer_class = PetOwnerModelSerializer


class PetListCreateAPIView(generics.ListCreateAPIView):

    queryset = Pet.objects.all()
    serializer_class = PetListModelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "owner__first_name"]

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == "POST":
            serializer_class = PetModelSerializer

        return serializer_class


class PetDateListCreateAPIView(generics.ListCreateAPIView):

    queryset = PetDate.objects.all()
    serializer_class = PetDateListModelSerializer

    def get_queryset(self):
        pet_id = self.request.GET.get("pet")
        owner_id = self.request.GET.get("owner")
        filters = {}
        if pet_id:
            filters["pet_id"] = pet_id

        if owner_id:
            filters["pet__owner_id"] = owner_id

        return self.queryset.filter(**filters)

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == "POST":
            serializer_class = PetDateModelSerializer

        return serializer_class


class PetDateRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    http_method_names = ["get", "patch", "delete"]
    queryset = PetDate.objects.all()
    serializer_class = PetDatePetRetrieveModelSerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == "PATCH":
            serializer_class = PetDatePartialUpdateModelSerializer

        return serializer_class


# ENDPOINTS
# 1. Retrieve all dates given the owner name
